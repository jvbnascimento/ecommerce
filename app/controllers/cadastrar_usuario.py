from app import app
from app import db

from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user

from app.controllers.forms import RegistrationForm

from app.models.usuario import Usuario

current_port = '8080/'

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_usuario():
    if current_user.is_authenticated:
        return redirect(url_for('index_user'))

    form = RegistrationForm()
    current_url = request.url.split(current_port)
    current_url = current_url[1]

    if form.validate_on_submit():
        usuario = Usuario(nome=form.nome.data, email=form.email.data, tipo=2)
        usuario.set_senha(form.senha.data)
        db.session.add(usuario)
        db.session.commit()

        flash('Parabéns, seu cadastro foi concluído com êxito!')
        return redirect(url_for('login'))

    return render_template(
        'cadastro_usuario.html', 
        title = 'Ecommerce - Cadastre-se', 
        form = form, 
        url = current_url
    )