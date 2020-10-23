### [OLXCRAPPER](https://github.com/yagolimalins/olxcrapper)

## Introdução

Script em Python + Beautiful Soup que realiza consultas exaustivas em categorias da OLX em busca de anúncios novos,
ao encontrar um novo anúncio nessa categoria, ele usa as credenciais de login do GMail fornecidas nas variáveis do script
para enviar para o próprio usuário um Email com informações sobre o novo produto da categoria.

## Requisitos

Esse script depende do Python e dos módulos: bs4, requests, lxml, argparse.

O usuário tem que usar uma conta do GMail, por enquanto é o unico servidor suportado.

## Instalação e uso

```sh
pip install olxcrapper
olxcrapper -g seuemail@gmail.com -s senhadogmail -u https://sp.olx.com.br/celulares -t 60
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

* O script irá executar continuamente e irá atualizar a lista a cada -t segundos, sempre que encontrar um
  anúncio novo na categoria referida pelo usuário, o mesmo enviará um email para a caixa de entrada do GMail indicado,
  esse script só enviará email caso haja um anuncio novo, assim evitando floodar a caixa de entrada.

OBS: é importante inserir os dados de login corretamente, caso estejam incorretos, o script executará, mostrará
a listagem de anúncios mas não conseguirá notificar por email. Também é interessante deixar o argumento -t com valor 60
pois a listagem da olx só atualiza a cada 1 minuto, valores menores que 60 segundos pode causar mau comportamento do script.

## Proxy
Caso necessite realizar a requisção através de um proxy, o parametro -p recebe uma string com a configuração de proxy, seja com autenticação
ou não. Exemplo:
```
-p http://ip:porta
```
Ou ainda:
```
-p http://usuario:senha@ip:porta
```

## Autor

**Yago Lima Lins**

* Github: [@yagolimalins](https://github.com/yagolimalins)

## Contribua com o projeto

Contribuições, bugs e pedidos de novas funcionalidades são bem vindos!
Sinta-se a vontade para conferir: [issues page](https://github.com/yagolimalins/olxcrapper/issues). 

## Apoie o autor

Considere fazer uma contribuição no patreon caso esse script seja útil pra você :)

**https://www.patreon.com/yagolimalins**

## Licença

Copyright © 2020 [Yago Lima Lins](https://github.com/yagolimalins).
This project is [GNU](https://www.gnu.org/licenses/gpl-3.0.pt-br.html) licensed.

***
