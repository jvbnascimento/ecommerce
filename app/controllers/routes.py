from flask import render_template, flash, redirect, request

from app import app

from app.models.login import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = ''#{'username': 'João Vitor'}
    form = LoginForm(request.form)
    
    return render_template('index.html', title='Ecommerce - Página Inicial', user=user, form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        flash('Login solicitado por email {}, lembrar_me={}'.format(
            form.email.data, form.lembrar_me.data))
        return redirect('/index')

    return render_template('modelo_login.html', title='Sign In', form = form)