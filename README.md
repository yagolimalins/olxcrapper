<h1 align="center">OL' X-CRAPPER
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://www.gnu.org/licenses/gpl-3.0.pt-br.html" target="_blank">
    <img alt="License: GNU" src="https://img.shields.io/badge/License-GNU-yellow.svg" />
  </a>
</p>

</h1>

> Script de Web Scraping em Python para categorias da OLX com notificações de novos anúncios por EMAIL 

### [Homepage](https://github.com/yagolimalins/OLXCRAPPER)

## Instruções

```sh
Esse script depende do Python e dos módulos: bs4, smtplib, email, requests, time. 

Mude a variavel URL do script para o link da categoria da OLX que deseja fazer scraping. 

Esse script utiliza-se das variáveis de ambiente EMAIL_USER e EMAIL_PASS para 
login e envio dos emails de notificação de novos anúncios da categoria selecionada,
adicione as variáveis de ambiente ao seu sistema, onde EMAIL_USER é a variável que irá 
armazenar o seu endereço de email, e EMAIL_PASS armazenará a senha do seu email, 
variáveis de ambiente são utilizadas nesse script para que seus dados pessoais 
não sejam expostos no código. 

OBS: ESSE SCRIPT USA O SERVIDOR DO GMAIL, UTILIZE DADOS DE UMA CONTA GOOGLE AO DEFINIR 
AS VARIÁVEIS DE AMBIENTE EMAIL_USER e EMAIL_PASS NO SISTEMA.
```

## Instalação e uso

Após instaladas todas as dependências necessárias 
e configurar as variáveis de ambiente, execute os comandos:
```sh
git clone https://github.com/yagolimalins/OLXCRAPPER.git
cd OLXCRAPPER
python ./OLXCRAPPER.py
```

## Autor

**Yago Lima Lins**

* Github: [@yagolimalins](https://github.com/yagolimalins)

## Contribua com o projeto

Contribuições, bugs e pedidos de novas funcionalidades são bem vindos! <br />
Sinta-se a vontade para conferir: [issues page](https://github.com/yagolimalins/OLXCRAPPER/issues). 

## Apoie o autor

Deixe uma estrela se esse projeto te ajudou! :)

<a href="https://www.patreon.com/yagolimalins">
  <img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

## Licença

Copyright © 2020 [Yago Lima Lins](https://github.com/yagolimalins).<br />
This project is [GNU](https://www.gnu.org/licenses/gpl-3.0.pt-br.html) licensed.

***