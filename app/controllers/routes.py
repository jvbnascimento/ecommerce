import os

from app import app
from app import db

from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_user, logout_user, login_required

from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename

from app.controllers.forms import LoginForm, RegistrationForm, CadastroProdutoForm

from app.models.usuario import Usuario
from app.models.produto import Produto
from app.models.categoria import Categoria

dirpath = os.getcwd()
UPLOAD_FOLDER = dirpath + '\\app\\static\\img\\'

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('index_user'))

    form = LoginForm()
    usuario = ''

    current_url = request.url.split('5500/')
    current_url = current_url[1]

    lista_produtos = Produto.query.all()

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

    return render_template('index.html', title='Ecommerce - Página Inicial', user=usuario, form=form, url=current_url, produtos=lista_produtos)


@app.route('/user')
def index_user():
    if current_user.is_authenticated:
        current_url = request.url.split('5500/')
        current_url = current_url[1]

        lista_produtos = Produto.query.all()

        return render_template('index.html', title='Ecommerce - Página Inicial - ' + current_user.nome, user=current_user, url=current_url, produtos=lista_produtos)
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index_user'))

    form = LoginForm()
    current_url = request.url.split('5500/')
    current_url = current_url[1]

    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()

        if usuario is None or not usuario.check_senha(form.senha.data):
            flash('Email ou senha inválidos')
            return redirect(url_for('login'))

        login_user(usuario, remember=form.lembrar_me.data)
        return redirect(url_for('index_user'))

    return render_template('login.html', title='Ecommerce - Página Inicial', form=form, url=current_url)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_usuario():
    if current_user.is_authenticated:
        return redirect(url_for('index_user'))

    form = RegistrationForm()
    current_url = request.url.split('5500/')
    current_url = current_url[1]

    if form.validate_on_submit():
        usuario = Usuario(nome=form.nome.data, email=form.email.data, tipo=2)
        usuario.set_senha(form.senha.data)
        db.session.add(usuario)
        db.session.commit()

        flash('Parabéns, seu cadastro foi concluído com êxito!')
        return redirect(url_for('login'))

    return render_template('cadastro_usuario.html', title='Ecommerce - Cadastre-se', form=form, url=current_url)


@app.route('/user/gerenciar_estoque', methods=['GET', 'POST'])
def gerenciar_estoque():
    if current_user.is_authenticated and current_user.tipo == 1:
        current_url = request.url.split('5500/')
        current_url = current_url[1]

        form = CadastroProdutoForm()
        lista_produtos = Produto.query.all()

        if form.validate_on_submit():
            if not request.files:
                redirect(url_for('gerenciar_estoque'))

            imagem_upada = request.files['imagem']
            nome_imagem = secure_filename(imagem_upada.filename)

            imagem_upada.save(os.path.join(UPLOAD_FOLDER, nome_imagem))

            c = Categoria(nome='Teste')

            produto = Produto(descricao=form.descricao.data, quantidade=form.quantidade.data, preco=form.preco.data, imagem=(nome_imagem), categorias_produto=[c])

            db.session.add(produto)
            db.session.commit()

            flash('Parabéns, seu produto foi cadastrado com sucesso!')
            return redirect(url_for('index_user'))

        return render_template('gerenciar_estoque.html', title='Ecommerce - Estoque', url=current_url, user=current_user, form=form, produtos=lista_produtos)
    flash('Você não é um administrador do sistema.')
    return redirect(url_for('index_user'))
