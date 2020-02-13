from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_user, logout_user

from app import app

from app.controllers.forms import LoginForm
from app.models.usuario import Usuario

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('index_user'))
    
    form = LoginForm(request.form)
    usuario = ''

    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email = form.email.data).first()

        if usuario is None or not usuario.check_senha(form.senha.data):
            flash('Email ou senha inválidos')
            return redirect(url_for('login'))
        
        login_user(usuario, remember = form.lembrar_me.data)
        return redirect(url_for('index_user'))

    return render_template('index.html', title='Ecommerce - Página Inicial', user=usuario, form=form)

@app.route('/user')
def index_user():
    if current_user.is_authenticated:
        return render_template('index.html', title='Ecommerce - Página Inicial - ' + current_user.nome, user=current_user)
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index_user'))
    
    form = LoginForm(request.form)

    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email = form.email.data).first()

        if usuario is None or not usuario.check_senha(form.senha.data):
            flash('Email ou senha inválidos')
            return redirect(url_for('login'))
        
        login_user(usuario, remember = form.lembrar_me.data)
        return redirect(url_for('index_user'))

    return render_template('login.html', title='Ecommerce - Página Inicial', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))