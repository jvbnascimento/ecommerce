import json

from app import app

from flask import request, make_response, url_for, redirect

current_port = '8080/'

@app.route('/remover_carrinho/produto/', methods=['GET', 'POST'])
def remover_carrinho():
    cookie = request.cookies.get('carrinho_compras')
    
    if request.method == "POST":
        produto_remover = request.get_json()
        produto_remover = str(produto_remover).replace("'", "\"")

        dados_json = json.loads(produto_remover)

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

            quantidade_produtos_carrinho.pop(id_produtos_carrinho.index(produto[0]))
            id_produtos_carrinho.pop(id_produtos_carrinho.index(produto[0]))

            novoCookie = ""
            total_itens = 0
            
            for c in range(len(id_produtos_carrinho)):
                novoCookie += str(id_produtos_carrinho[c]) + "_" + str(quantidade_produtos_carrinho[c]) + ";"
                total_itens += int(quantidade_produtos_carrinho[c])
            
            resposta = make_response(str(total_itens))
            resposta.set_cookie('carrinho_compras', novoCookie)

            return resposta
        return redirect(url_for('index'))