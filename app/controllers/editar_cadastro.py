import os

from app import app
from app import db

from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_required

from app.controllers.forms import EditarDadosUsuarioForm

from app.models.usuario import Usuario

current_port = '8080/'


@app.route('/user/gerenciar_cadastros/editar_dados/<id>', methods=['GET', 'POST'])
@login_required
def editar_cadastro(id):
    if current_user.is_authenticated and current_user.tipo == 1 or current_user.tipo == 2:
        current_url = request.url.split(current_port)
        current_url = current_url[1]

        usuario = Usuario.query.filter_by(id = id).first_or_404()

        form = EditarDadosUsuarioForm()

        if form.validate_on_submit():
            usuario.nome = form.nome.data
            usuario.email = form.email.data

            db.session.add(usuario)
            db.session.commit()
            flash('As alterações foram salvadas com sucesso.')
            return redirect(url_for('editar_cadastro', id = usuario.id))
        
        elif request.method == 'GET':
            form.nome.data = usuario.nome
            form.email.data = usuario.email
        
        return render_template(
            'editar_cadastro.html', 
            title = 'Ecommerce - Cadastros', 
            url = current_url, 
            user = current_user, 
            form = form, 
            usuario = usuario
        )
    
    flash('Você precisa estar logado para realizar esta ação.')
    return redirect(url_for('index_user'))
