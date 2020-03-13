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
            lista_cookie = cookie.split(";")

            lista_cookie.pop(len(lista_cookie) - 1)

            id_produtos_carrinho = []
            quantidade_produtos_carrinho = []

            for p in lista_cookie:
                item = p.split("_")

                id_produtos_carrinho.append(int(item[0]))
                quantidade_produtos_carrinho.append(int(item[1]))
            
            produto = []
            for p in dados_json:
                produto.append(dados_json[p])

            if produto[0] in id_produtos_carrinho:
                quantidade_produtos_carrinho[id_produtos_carrinho.index(produto[0])] += produto[1]
            else:
                id_produtos_carrinho.append(produto[0])
                quantidade_produtos_carrinho.append(produto[1])

            novoCookie = ""
            total_itens = 0
            
            for c in range(len(id_produtos_carrinho)):
                novoCookie += str(id_produtos_carrinho[c]) + "_" + str(quantidade_produtos_carrinho[c]) + ";"
                total_itens += int(quantidade_produtos_carrinho[c])
            
            resposta = make_response(str(total_itens))
            resposta.set_cookie('carrinho_compras', novoCookie)

            return resposta
        else:
            produto = []
            for p in dados_json:
                produto.append(dados_json[p])
            
            novoCookie = ""
            total_itens = 0

            for p in range(len(produto)):
                novoCookie += str(produto[p])

                if ((p+1) < len(produto)):
                    novoCookie += "_"
            novoCookie += ";"

            total_itens = int(produto[1])

            resposta = make_response(str(total_itens))
            resposta.set_cookie('carrinho_compras', novoCookie)

            return resposta