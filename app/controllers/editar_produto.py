import os

from app import app
from app import db

from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

from app.controllers.forms import EditarDadosProdutoForm

from app.models.produto import Produto
from app.models.categoria import Categoria

dirpath = os.getcwd()
UPLOAD_FOLDER = dirpath + '/app/static/img/'
current_port = '8080/'


@app.route('/user/gerenciar_estoque/editar_produto/<id>', methods=['GET', 'POST'])
@login_required
def editar_produto(id):
    if current_user.is_authenticated and current_user.tipo == 1:
        current_url = request.url.split(current_port)
        current_url = current_url[1]

        produto = Produto.query.filter_by(id = id).first_or_404()
        categorias = Categoria.query.order_by('nome').all()

        form = EditarDadosProdutoForm()

        if form.validate_on_submit():
            imagem_upada = ""

            if request.files and request.files['imagem'].filename != "":
                imagem_upada = request.files['imagem']
                nome_imagem = secure_filename(imagem_upada.filename)

                imagem_upada.save(os.path.join(UPLOAD_FOLDER, nome_imagem))

            c = Categoria(nome='Teste')
            
            produto.descricao = form.descricao.data
            produto.quantidade = form.quantidade.data
            produto.preco = form.preco.data

            db.session.add(produto)
            db.session.commit()
            flash('As alterações foram salvadas com sucesso.')
            return redirect(url_for('editar_produto', id = produto.id))
        elif request.method == 'GET':
            form.descricao.data = produto.descricao
            form.quantidade.data = produto.quantidade
            form.preco.data = produto.preco
        
        return render_template(
            'editar_produto.html', 
            title='Ecommerce - Estoque', 
            url=current_url, 
            user=current_user, 
            form = form, 
            produto = produto, 
            categorias = categorias
        )
    
    flash('Você não é um administrador do sistema.')
    return redirect(url_for('index_user'))
