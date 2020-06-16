<h1 align="center">OL' X-CRAPPER
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://www.gnu.org/licenses/gpl-3.0.pt-br.html" target="_blank">
    <img alt="License: GNU" src="https://img.shields.io/badge/License-GNU-yellow.svg" />
  </a>
</p>

</h1>

### [Homepage](https://github.com/yagolimalins/olxcrapper)

## Introdução

Script em Python + Beautiful Soup que realiza consultas exaustivas em categorias da OLX em busca de anúncios novos,
ao encontrar um novo anúncio nessa categoria, ele usa as credenciais de login do GMail fornecidas nas variáveis do script
para enviar para o próprio usuário um Email com informações sobre o novo produto da categoria.

## Requisitos

Esse script depende do Python e dos módulos: bs4, requests, lxml, argparse.

O usuário tem que usar uma conta do GMail, por enquanto é o unico servidor suportado.

## Instalação e uso

Certifique-se de que tem instalados o git e python instalados, após isso installe as dependências 
requeridas pelo script utilizando os seguintes comandos no terminal:

```sh
python -m pip install bs4 requests lxml argparse
```

Após isso você já pode clonar o repositório e utilizar o script como exemplificado abaixo:

```sh
git clone https://github.com/yagolimalins/olxcrapper.git
cd olxcrapper
python ./olxcrapper.py -g seuemail@gmail.com -s senhadogmail -u https://sp.olx.com.br/celulares
```

Substitua os dados de login acima com suas credenciais do gmail e com o link da categoria desejada.

* Quanto a conta do GMail, sugiro criar uma nova conta pra uso desse script para que sua caixa de entrada
  não seja floodada com emails do tipo, é importante que na conta do GMail utilizada esteja habilitada
a opção de acesso de apps menos confiáveis.

* Caso deseje mais segurança ao utilizar sua conta, habilite
  a opção de autenticação de dois fatores e crie uma senha exclusiva para o uso desse script, esse tipo de senha
  é gerada automaticamente pela conta da google e tem 16 caracteres, ex: "gzhupbrkrdbfhpiy", você pode gerar
  uma senha de app aqui: https://security.google.com/settings/security/apppasswords

* Quanto ao link da categoria da olx desejada, para obter um link utilizável, acesse a categoria da olx desejada
escolha seu estado e/ou cidade e copie o link do navegador pra substituir no comando exemplificado acima.

* O script irá executar continuamente e irá atualizar a lista a cada 5 segundos, sempre que encontrar um
  anúncio novo na categoria referida pelo usuário, o mesmo enviará um email para a caixa de entrada do GMail indicado,
  esse script só enviará email caso haja um anuncio novo, assim evitando floodar a caixa de entrada.

OBS: é importante inserir os dados de login corretamente, caso estejam incorretos, o script executará, mostrará
a listagem de anúncios mas não conseguirá notificar por email.


## Autor

**Yago Lima Lins**

* Github: [@yagolimalins](https://github.com/yagolimalins)

## Contribua com o projeto

Contribuições, bugs e pedidos de novas funcionalidades são bem vindos! <br />
Sinta-se a vontade para conferir: [issues page](https://github.com/yagolimalins/olxcrapper/issues). 

## Apoie o autor

Deixe uma estrela se esse projeto te ajudou! :)

<a href="https://www.patreon.com/yagolimalins">
  <img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

## Licença

Copyright © 2020 [Yago Lima Lins](https://github.com/yagolimalins).<br />
This project is [GNU](https://www.gnu.org/licenses/gpl-3.0.pt-br.html) licensed.

***
