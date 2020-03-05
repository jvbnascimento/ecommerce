from app import app

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user
from werkzeug.urls import url_parse

from app.controllers.forms import LoginForm
from app.models.usuario import Usuario
from app.models.produto import Produto
from app.models.categoria import Categoria

current_port = '8080/'

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('index_user'))

    form = LoginForm()
    usuario = ''

    current_url = request.url.split(current_port)
    current_url = current_url[1]

    lista_produtos = Produto.query.order_by('descricao').all()
    categorias = Categoria.query.order_by('nome').all()

    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()

        if usuario is None or not usuario.check_senha(form.senha.data):
            flash('Email ou senha inválidos')
            return redirect(url_for('login'))

        login_user(usuario, remember=form.lembrar_me.data)
        next_page = request.args.get('next')

        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template(
        'index.html', 
        title ='Ecommerce - Página Inicial', 
        user = usuario, 
        form = form, 
        url = current_url, 
        produtos = lista_produtos, 
        categorias = categorias
    )