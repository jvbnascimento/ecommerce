import os

from app import app
from app import db

from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

from app.controllers.forms import CadastroProdutoForm

from app.models.produto import Produto
from app.models.categoria import Categoria

dirpath = os.getcwd()
UPLOAD_FOLDER = dirpath + '/app/static/img/'
current_port = '8080/'

@app.route('/user/gerenciar_estoque', methods=['GET', 'POST'])
@login_required
def gerenciar_estoque():
    if current_user.is_authenticated and current_user.tipo == 1:
        current_url = request.url.split(current_port)
        current_url = current_url[1]

        form = CadastroProdutoForm()

        lista_produtos = Produto.query.order_by('descricao').all()
        categorias = Categoria.query.order_by('nome').all()

        if form.validate_on_submit():
            if not request.files:
                redirect(url_for('gerenciar_estoque'))

            imagem_upada = request.files['imagem']
            nome_imagem = secure_filename(imagem_upada.filename)

            imagem_upada.save(os.path.join(UPLOAD_FOLDER, nome_imagem))

            if not request.form["categorias_selecionadas"]:
                redirect(url_for('gerenciar_estoque'))
            
            lista_categorias_temp = request.form["categorias_selecionadas"].split(';')

            lista_categorias_temp.pop(len(lista_categorias_temp)-1)

            produto = Produto(
                descricao = form.descricao.data, 
                quantidade = form.quantidade.data,
                preco = form.preco.data, 
                imagem = (nome_imagem)
            )

            for c in lista_categorias_temp:
                item = c.split("_")

                categoria = Categoria.query.filter_by(id = item[1]).first_or_404()

                produto.categorias_produto.append(categoria)

            db.session.add(produto)
            db.session.commit()

            flash('Parabéns, seu produto foi cadastrado com sucesso!')
            return redirect(url_for('index_user'))

        return render_template(
            'gerenciar_estoque.html', 
            title='Ecommerce - Estoque', 
            url = current_url, 
            user = current_user, 
            form = form, 
            produtos = lista_produtos,
            categorias = categorias
        )
    flash('Você não é um administrador do sistema.')
    return redirect(url_for('index_user'))