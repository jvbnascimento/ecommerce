from app import app

from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user

from app.models.produto import Produto
from app.models.categoria import Categoria

current_port = '8080/'


@app.route('/user/categoria/<id>', methods=['GET', 'POST'])
def categoria(id):
    if current_user.is_authenticated or current_user.is_anonymous:
        current_url = request.url.split(current_port)
        current_url = current_url[1]

        produtos_categoria = Produto.query.join(
            Categoria.produtos).filter(Categoria.id == id).all()
        categorias = Categoria.query.order_by('nome').all()

        cookie = request.cookies.get('carrinho_compras')

        total_itens = 0

        if (cookie):
            lista_cookie = cookie.split(";")

            lista_cookie.pop(len(lista_cookie) - 1)

            for p in lista_cookie:
                item = p.split("_")
                total_itens += int(item[1])

        return render_template(
            'categoria.html',
            title = 'Ecommerce - ' +
                produtos_categoria[0].categorias_produto[0].nome,
            url = current_url,
            user = current_user,
            produtos_categoria = produtos_categoria,
            categorias = categorias,
            total_itens = total_itens
        )
