import json
from datetime import datetime

from app import app
from app import db

from flask import request, make_response, url_for, redirect, flash
from flask_login import current_user

from app.models.compra import Compra, CompraProduto
from app.models.produto import Produto

current_port = '8080/'


@app.route('/carrinho_compras/finalizar_compra/', methods=['GET', 'POST'])
def finalizar_compra():
    if current_user.is_authenticated and current_user.tipo == 2:
        current_url = request.url.split(current_port)
        current_url = current_url[1]

        cookie = request.cookies.get('carrinho_compras')

        lista_cookie = cookie.split(";")

        lista_cookie.pop(len(lista_cookie) - 1)

        id_produtos_carrinho = []
        quantidade_produtos_carrinho = []

        total_itens = 0

        for p in lista_cookie:
            item = p.split("_")

            id_produtos_carrinho.append(int(item[0]))
            quantidade_produtos_carrinho.append(int(item[1]))

            total_itens += int(item[1])

        data_compra = datetime.now()

        compra = Compra(
            data = data_compra,
            total_itens = total_itens,
            usuario_id = current_user.id
        )

        for i in id_produtos_carrinho:
            produto = Produto.query.filter_by(id = i).first_or_404()

            compra_produto = CompraProduto(
                quantidade_item = quantidade_produtos_carrinho[
                    id_produtos_carrinho.index(i)
                ],
                preco_item = produto.preco
            )
            compra_produto.produto = produto
            compra.produtos_compra.append(compra_produto)

        db.session.add(compra)
        db.session.commit()

        flash('Compra finalizada com sucesso.')
        
        resposta = make_response(redirect(url_for('index_user')))
        resposta.set_cookie('carrinho_compras', '')
        
        return resposta

    flash('Para finalizar uma compra, você deve estar logado em sua conta.')
    return redirect(url_for('login'))
