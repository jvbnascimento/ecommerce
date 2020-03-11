import json

from app import app

from flask import flash, request, render_template, make_response, url_for, redirect

from app.models.usuario import Usuario
from app.models.categoria import Categoria
from app.controllers.forms import LoginForm

current_port = '8080/'

@app.route('/adicionar_carrinho/produto/', methods=['GET', 'POST'])
def adicionar_carrinho():
    cookie = request.cookies.get('carrinho_compras')
    
    if request.method == "POST":
        produto_adicionar = request.get_json()
        produto_adicionar = str(produto_adicionar).replace("'", "\"")

        dados_json = json.loads(produto_adicionar)

        if (cookie):
            print ("cookie antigo: " + str(cookie))

            lista_cookie = cookie.split(";")

            print ("transformando: " + str(lista_cookie))

            lista_cookie.pop(len(lista_cookie) - 1)

            print ("lista cookie: " + str(lista_cookie))

            produtos_carrinho = []
            for p in lista_cookie:
                item = p.split("_")

                produtos_carrinho.append(int(item[0]))
                produtos_carrinho.append(int(item[1]))

            produto = []
            for p in dados_json:
                produto.append(dados_json[p])

            if produto[0] in produtos_carrinho:
                for p in range(0, len(produtos_carrinho), 2):
                    if produtos_carrinho[p] == produto[0]:
                        produtos_carrinho[p + 1] += produto[1]

            else:
                produtos_carrinho.append(produto[0])
                produtos_carrinho.append(produto[1])

            novoCookie = ""
            for c in range(0, len(produtos_carrinho), 2):
                novoCookie += str(produtos_carrinho[c]) + "_" + str(produtos_carrinho[c + 1]) + ";"

            resposta = make_response("200 | OK")
            resposta.set_cookie('carrinho_compras', novoCookie)

            print ("cookie atual: " + str(novoCookie))
            print("")

            return resposta
        else:
            produto = []
            for p in dados_json:
                produto.append(dados_json[p])
            
            novoCookie = ""
            for p in range(len(produto)):
                novoCookie += str(produto[p])

                if ((p+1) < len(produto)):
                    novoCookie += "_"
            novoCookie += ";"

            resposta = make_response("200 | OK")
            resposta.set_cookie('carrinho_compras', novoCookie)

            return resposta