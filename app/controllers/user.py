from app import app

from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_required

from app.models.produto import Produto

current_port = '8080/'

@app.route('/user')
@login_required
def index_user():
    if current_user.is_authenticated:
        current_url = request.url.split(current_port)
        current_url = current_url[1]

        lista_produtos = Produto.query.order_by('id').all()

        return render_template(
            'index.html', 
            title = 'Ecommerce - Página Inicial', 
            user = current_user, 
            url = current_url, 
            produtos = lista_produtos
        )
    return redirect(url_for('index'))