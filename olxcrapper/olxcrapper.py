# OLXCRAPPER - Ferramenta de scraping de categorias da OLX com suporte a notificação de novos anúncios pelo GMail
# Copyright (C) 2020  Yago Lima Lins

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see https://www.gnu.org/licenses/gpl-3.0.html

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
    parser.add_argument('-t', '--timesleep', type=int, metavar='', required=True, help='Tempo entre atualizações de lista (em segundos)')
    parser.add_argument('-p', '--proxy', type=str, metavar='', required=False, help='Utilizar proxy para realizar as requisições')

    args = parser.parse_args()

    URL = args.url
    EMAIL_ADDRESS = args.gmail
    EMAIL_PASSWORD = args.senha
    timesleep = args.timesleep
    proxy = args.proxy
    
    if proxy is not None:
        proxies = {"http": proxy, "https": proxy}

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}

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
        print("Ferramenta de scraping de categorias da OLX com suporte a notificação de novos anúncios pelo GMail")
        print("Autor: Yago Lima Lins | yago.lima.lins@protonmail.com | https://github.com/yagolimalins/olxcrapper")
        print("-------------------------------------------------------------------------------------------------\n")


    def screen_clear():
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('cls')


    def statuscode(URL=URL, headers=headers):
        result = makeRequest()
        statuscodenumber = int(result.status_code)

        return(statuscodenumber)

    def webscrap(URL=URL, headers=headers):
        result = makeRequest()
        src = result.content
        soup = BeautifulSoup(src, 'lxml') # Usando o parser do BS4, alternativamente usar: (src, 'lxml')
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

    def makeRequest(URL=URL, headers=headers, proxy=proxy):
        if proxy is None:
            result = requests.get(URL, headers=headers)
        else:
            result = requests.get(URL, headers=headers, proxies=proxies)

        return(result)

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

            if listaNew[0][2] != listaOld[0][2]:
                print("O item mais recentemente anunciado é: " + listaNew[0][0] + " - " + listaNew[0][1])
                #------------------------ EMAIL -------------------------------
                msg = EmailMessage()
                msg['Subject'] = "[OLXCRAPPER] " + listaNew[0][0] + " - " + listaNew[0][1]
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = EMAIL_ADDRESS
                msg.set_content('Link para o anuncio: ' + listaNew[0][2])
                
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    smtp.send_message(msg)
                #--------------------------------------------------------------
                listaOld = listaNew
            
            elif listaNew[0][0] == listaOld[0][0]:
                print("O item mais recentemente anunciado continua sendo: " + listaOld[0][0] + " - " + listaOld[0][1])
        
        else:
            print("O site retornou código de status: " + str(statuscodenumber))

        time.sleep(timesleep)

if __name__ == "__main__":
    main()
