import os
import time
import smtplib
import argparse
import requests
from getpass import getpass
from bs4 import BeautifulSoup
from email.message import EmailMessage

def main():

    # DECLARAÇÃO E INICIALIZAÇÃO DE VARIÁVEIS:


    parser = argparse.ArgumentParser(description='Dados do GMail e URL da categoria')
    parser.add_argument('-u', '--url', type=str, metavar='', required=True, help='Link da categoria da OLX (ex: https://sp.olx.com.br/celulares')
    parser.add_argument('-g', '--gmail', type=str, metavar='', required=True, help='Endereço do GMail')
    parser.add_argument('-s', '--senha', type=str, metavar='', required=True, help='Senha do GMail')
    parser.add_argument('-t', '--timesleep', type=str, metavar='', required=True, help='Tempo entre atualizações')

    args = parser.parse_args()

    URL = args.url
    EMAIL_ADDRESS = args.gmail
    EMAIL_PASSWORD = args.senha
    timesleep = args.timesleep

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}


    # DECLARAÇÃO DE FUNÇÕES:


    def banner():

        print("╔═══════════════════════════════════════════════════════════════════════════════════════════════╗")
        print("║  ██████╗ ██╗    ██╗     ██╗  ██╗      ██████╗██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗  ║")
        print("║ ██╔═══██╗██║    ╚═╝      ██╗██╔╝     ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗ ║")
        print("║ ██║   ██║██║              ███╔╝█████╗██║     ██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝ ║")
        print("║ ██║   ██║██║             ██╔██╗╚════╝██║     ██╔══██╗██╔══██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗ ║")
        print("║ ╚██████╔╝███████╗       ██╔╝ ██╗     ╚██████╗██║  ██║██║  ██║██║     ██║     ███████╗██║  ██║ ║")
        print("║  ╚═════╝ ╚══════╝       ╚═╝  ╚═╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝ ║")
        print("╚═══════════════════════════════════════════════════════════════════════════════════════════════╝")
        print("  Ferramenta de busca por novos anúncios em categorias da OLX com notificações por email (GMail) ")
        print("Autor: Yago Lima Lins | yago.lima.lins@protonmail.com | https://github.com/yagolimalins/olxcrapper")
        print("-------------------------------------------------------------------------------------------------\n")


    def screen_clear():
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('cls')


    def statuscode(URL=URL, headers=headers):

        result = requests.get(URL, headers=headers)
        statuscodenumber = int(result.status_code)

        return(statuscodenumber)

    def webscrap(URL=URL, headers=headers, ):

        result = requests.get(URL, headers=headers)
        src = result.content
        soup = BeautifulSoup(src, 'lxml')
        items = soup.find_all('a')
        lista = []

        for item in items:

                if ("Hoje" and "R$") in item.text:

                        title = item.get('title')
                        price = item.find('p').get_text()
                        URL = item.attrs['href']
                        lista.append([title, price, URL])

                        print(price + ' - ' + title)
            
        
        print("\n-------------------------------------------------------------------------------------------------")

        return(lista)


    # EXECUÇÃO DO SCRIPT:


    banner()

    listaOld = webscrap()
    print("O item mais recentemente adicionado é: " + listaOld[0][0] + " - " + listaOld[0][1])

    time.sleep(timesleep)

    while True:

        screen_clear()

        banner()
        
        statuscodenumber = statuscode()

        if statuscodenumber == 200:
            listaNew = webscrap()

            if listaNew[0][0] != listaOld[0][0]:
                print("O item mais recentemente anunciado é: " + listaNew[0][0] + " - " + listaNew[0][1])
                
                msg = EmailMessage()
                msg['Subject'] = "[OLXCRAPPER] " + listaNew[0][0] + " - " + listaNew[0][1]
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = EMAIL_ADDRESS
                msg.set_content('Link para o anuncio: ' + listaNew[0][2])

                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    smtp.send_message(msg)

                listaOld = listaNew
            
            elif listaNew[0][0] == listaOld[0][0]:
                print("O item mais recentemente anunciado continua sendo: " + listaOld[0][0] + " - " + listaOld[0][1])
        
        else:
            print("O site retornou código de status: " + str(statuscodenumber))

        time.sleep(timesleep)

if __name__ == "__main__":
	main()
