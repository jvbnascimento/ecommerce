from app import app
from app import db

from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_required

# from app.controllers.forms import CadastroProdutoForm

from app.models.compra import Compra, CompraProduto

current_port = '8080/'


@app.route('/user/minhas_compras', methods=['GET', 'POST'])
@login_required
def minhas_compras():
    if current_user.is_authenticated and current_user.tipo == 2:
        current_url = request.url.split(current_port)
        current_url = current_url[1]

        lista_compras = Compra.query.filter_by(
            usuario_id = current_user.id
        ).order_by('data').all()

        cookie = request.cookies.get('carrinho_compras')

        total_itens = 0

        if (cookie):
            lista_cookie = cookie.split(";")

            lista_cookie.pop(len(lista_cookie) - 1)

            for p in lista_cookie:
                item = p.split("_")
                total_itens += int(item[1])

        return render_template(
            'minhas_compras.html',
            title = 'Ecommerce - Minhas Compras',
            url = current_url,
            user = current_user,
            lista_compras = lista_compras,
            total_itens = total_itens
        )

    flash('Você não é um administrador do sistema.')
    return redirect(url_for('index_user'))
