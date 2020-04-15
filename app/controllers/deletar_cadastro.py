from app import app
from app import db

from flask import flash, redirect, request, url_for
from flask_login import current_user, login_required

from app.models.usuario import Usuario

current_port = '8080/'    

@app.route('/user/gerenciar_cadastros/deletar_cadastro/<id>', methods=['GET', 'POST'])
@login_required
def deletar_cadastro(id):
    if current_user.is_authenticated and current_user.tipo == 1:
        current_url = request.url.split(current_port)
        current_url = current_url[1]

        if request.method == 'GET':
            usuario = Usuario.query.filter_by(id = id).first_or_404()

            if usuario.tipo != 1:
                db.session.delete(usuario)
                db.session.commit()
                
                flash('Cadastro foi deletado com sucesso.')
                
                return redirect(url_for('gerenciar_cadastros'))
            
            flash('Você não pode deletar o perfil de administrador.')
            return redirect(url_for('gerenciar_cadastros'))

    flash('Você não é um administrador do sistema.')
    return redirect(url_for('index_user'))