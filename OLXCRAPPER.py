import requests
import time
from bs4 import BeautifulSoup
import os
import smtplib
from email.message import EmailMessage

url = "https://al.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios" # <- MUDE O LINK DE ACORDO COM A CATEGORIA DESEJADA

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'} 


def webscraper(url=url, headers=headers):

    print()
    print(" ██████╗ ██╗    ██╗     ██╗  ██╗      ██████╗██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗")
    print("██╔═══██╗██║    ╚═╝      ██╗██╔╝     ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗")
    print("██║   ██║██║              ███╔╝█████╗██║     ██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝")
    print("██║   ██║██║             ██╔██╗╚════╝██║     ██╔══██╗██╔══██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗")
    print("╚██████╔╝███████╗       ██╔╝ ██╗     ╚██████╗██║  ██║██║  ██║██║     ██║     ███████╗██║  ██║")
    print(" ╚═════╝ ╚══════╝       ╚═╝  ╚═╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝ \n")

    result = requests.get(url, headers=headers) #Faz uma requisição da página

    lista = [] # Inicia a variável lista onde serão armazenados os produtos, preços, etc em sublistas
    
    if result.status_code == 200: #Checa se a página está acessível

        # print("Código de status: 200 (URL Acessível) \n")

        src = result.content
        # print(src)

        soup = BeautifulSoup(src, 'lxml')

        links = soup.find_all('a') #Busca pela tag HTML 'a'
        #print(links)
        

        for link in links:

            if "R$" in link.text:
                title = link.get('title')
                price = link.find('p').get_text()
                url = link.attrs['href']
        
                print(price + ' - ' + title)
        
                lista.append([title, price, url])
            
        print("\n--------------------------------------------------------------------------------------") 
    
    else:
        
        print("URL Inacessível, código de erro: " + result.status_code)
        print("\n--------------------------------------------------------------------------------------")

    return(lista)


    
def sendmail(lista, EMAIL_ADDRESS=EMAIL_ADDRESS, EMAIL_PASSWORD=EMAIL_PASSWORD):

    msg = EmailMessage()
    msg['Subject'] = "[OL' X-CRAPPER] Novo item anunciado: " + lista[0][0] + " por " + lista[0][1]
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content('Link para o anuncio: ' + lista[0][2])

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        smtp.send_message(msg)


if __name__ == '__main__':

    lista3 = []

    while True:
        
        lista1 = webscraper()
        print("Item mais recentemente postado: " + lista1[0][0] + " por " + lista1[0][1])
        print("--------------------------------------------------------------------------------------")

        if lista1 != lista3:
            sendmail(lista1)
            lista3 = lista1 
        
        time.sleep(10)
        
        lista2 = webscraper()
        print("Item mais recentemente postado: " + lista2[0][0]  + " por " + lista2[0][1])
        print("--------------------------------------------------------------------------------------")

        if lista1 != lista2:
            sendmail(lista2)
            lista3 = lista2

        time.sleep(10)
