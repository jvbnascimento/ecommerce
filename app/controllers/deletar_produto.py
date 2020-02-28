from app import app
from app import db

from flask import flash, redirect, request, url_for
from flask_login import current_user, login_required

from app.models.produto import Produto

current_port = '8080/'    

@app.route('/user/gerenciar_estoque/deletar_produto/<id>', methods=['GET', 'POST'])
@login_required
def deletar_produto(id):
    if current_user.is_authenticated and current_user.tipo == 1:
        current_url = request.url.split(current_port)
        current_url = current_url[1]

        if request.method == 'GET':
            produto = Produto.query.filter_by(id = id).first_or_404()

            db.session.delete(produto)
            db.session.commit()
            
            flash('Produto foi deletado com sucesso.')
            
            return redirect(url_for('gerenciar_estoque'))

    flash('Você não é um administrador do sistema.')
    return redirect(url_for('index_user'))