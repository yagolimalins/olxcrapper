import requests
import time
from bs4 import BeautifulSoup
import os
import smtplib
from email.message import EmailMessage

url = "https://sp.olx.com.br/celulares" # <- MUDE O LINK DE ACORDO COM A CATEGORIA E ESTADO DESEJADOS 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'} 

EMAIL_ADDRESS = 'xxxxxx@gmail.com' # <- INSIRA SEU GMAIL ENTRE ASPAS COMO NO EXEMPLO
EMAIL_PASSWORD = 'xxxxxxxxxxxxxxxx' # <- INSIRA SUA SENHA ENTRE ASPAS COMO NO EXEMPLO

# Alternativamente você pode usar as variáveis de ambiente abaixo caso as mesmas estejam configuradas no sistema

#EMAIL_ADDRESS = os.environ.get('EMAIL_USER') 
#EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

def banner():

    print()
    print(" ██████╗ ██╗    ██╗     ██╗  ██╗      ██████╗██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗")
    print("██╔═══██╗██║    ╚═╝      ██╗██╔╝     ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗")
    print("██║   ██║██║              ███╔╝█████╗██║     ██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝")
    print("██║   ██║██║             ██╔██╗╚════╝██║     ██╔══██╗██╔══██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗")
    print("╚██████╔╝███████╗       ██╔╝ ██╗     ╚██████╗██║  ██║██║  ██║██║     ██║     ███████╗██║  ██║")
    print(" ╚═════╝ ╚══════╝       ╚═╝  ╚═╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝ \n")

def statuscode(url=url, headers=headers):

    result = requests.get(url, headers=headers)
    statuscodenumber = int(result.status_code)

    return(statuscodenumber)

def webscrap(url=url, headers=headers, ):

    result = requests.get(url, headers=headers)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    items = soup.find_all('a')
    lista = []

    for item in items:

            if "R$" in item.text:
                title = item.get('title')
                price = item.find('p').get_text()
                url = item.attrs['href']
        
                print(price + ' - ' + title)
        
                lista.append([title, price, url])

    return(lista)

def sendmail(lista, EMAIL_ADDRESS=EMAIL_ADDRESS, EMAIL_PASSWORD=EMAIL_PASSWORD):

    msg = EmailMessage()
    msg['Subject'] = "[OLXCRAPPER] Novo item: " + lista[0][0] + " - " + lista[0][1]
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content('Link para o anuncio: ' + lista[0][2])

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        smtp.send_message(msg)

def checkandsend(listaOld):
    listaNew = webscrap()
    if listaNew[0][0] != listaOld[0][0]:
        print("\n--------------------------------------------------------------------------------------")
        print("O item mais recentemente anunciado é: " + listaNew[0][0] + " - " + listaNew[0][1])
        sendmail(listaNew)
        global old 
        old = listaNew
    elif listaNew[0][0] == listaOld[0][0]:
        print("\n--------------------------------------------------------------------------------------")
        print("O item mais recentemente anunciado continua sendo: " + old[0][0] + " - " + old[0][1])
    
old = webscrap()

while True:
    
    banner()
    statuscodenumber = statuscode()
    if statuscodenumber == 200:
        checkandsend(old)
    else:
        print("Erro de conexão, código de status do site: " + str(statuscodenumber))

    time.sleep(10)
