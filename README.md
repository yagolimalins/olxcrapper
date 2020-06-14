<h1 align="center">OL' X-CRAPPER
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://www.gnu.org/licenses/gpl-3.0.pt-br.html" target="_blank">
    <img alt="License: GNU" src="https://img.shields.io/badge/License-GNU-yellow.svg" />
  </a>
</p>

</h1>

### [Homepage](https://github.com/yagolimalins/OLXCRAPPER)

## Introdução

Script em Python + Beautiful Soup que realiza consultas exaustivas em categorias da OLX em busca de anúncios novos
ao encontrar um novo anúncio nessa categoria, ele usa as credenciais de login do GMail fornecidas nas variáveis do script
para enviar para si mesmo um Email com informações sobre o novo produto da categoria.

## Requisitos

Esse script depende do Python e dos módulos: bs4, smtplib, email, requests, time. 

O usuário tem que usar uma conta do GMail, por enquanto é o unico servidor suportado.

## Instalação e uso

```sh
git clone https://github.com/yagolimalins/OLXCRAPPER.git
cd OLXCRAPPER
```

Edite o script OLXCRAPPER.py com o link da categoria da OLX que deseja fazer scraping, e com os dados
de login da conta Google, talvez seja necessário habilitar acesso de apps menos seguros na conta ou 
uma senha de app na conta Google para usar o script.

Após isso salve o arquivo e execute o seguinte comando no diretório do script:

```sh
python ./OLXCRAPPER.py
```
O script irá executar continuamente e irá atualizar a lista a cada 15 segundos, sempre que encontrar um
anúncio novo na categoria referida pela variável URL editada no script, ele enviará um email para o usuário
com as informações do anúncio.

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
