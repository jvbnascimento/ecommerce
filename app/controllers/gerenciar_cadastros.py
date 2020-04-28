from app import app
from app import db

from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_required

from app.models.usuario import Usuario

current_port = '8080/'

@app.route('/user/gerenciar_cadastros', methods=['GET', 'POST'])
@login_required
def gerenciar_cadastros():
    if current_user.is_authenticated and current_user.tipo == 1:
        current_url = request.url.split(current_port)
        current_url = current_url[1]

        lista_usuarios = Usuario.query.order_by('nome').all()

        return render_template(
            'gerenciar_cadastros.html', 
            title='Ecommerce - Cadastros', 
            url = current_url, 
            user = current_user,
            usuarios = lista_usuarios
        )
        
    flash('Você não é um administrador do sistema.')
    return redirect(url_for('index_user'))