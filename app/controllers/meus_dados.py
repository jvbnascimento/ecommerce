from app import app
from app import db

from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_required

from app.models.usuario import Usuario
from app.models.categoria import Categoria

from app.controllers.forms import EditarDadosUsuarioForm

current_port = '8080/'

@app.route('/user/meus_dados', methods=['GET', 'POST'])
@login_required
def meus_dados():
    if current_user.is_authenticated and current_user.tipo == 2:
        current_url = request.url.split(current_port)
        current_url = current_url[1]

        categorias = Categoria.query.order_by('nome').all()

        cookie = request.cookies.get('carrinho_compras')

        total_itens = 0

        if (cookie):
            lista_cookie = cookie.split(";")

            lista_cookie.pop(len(lista_cookie) - 1)

            for p in lista_cookie:
                item = p.split("_")
                total_itens += int(item[1])

        usuario = Usuario.query.filter_by(id = current_user.id).first_or_404()

        form = EditarDadosUsuarioForm()

        if form.validate_on_submit():
            usuario.nome = form.nome.data
            usuario.email = form.email.data

            db.session.add(usuario)
            db.session.commit()
            flash('As alterações foram salvadas com sucesso.')
            return redirect(url_for('meus_dados'))
        
        elif request.method == 'GET':
            form.nome.data = usuario.nome
            form.email.data = usuario.email

        return render_template(
            'meus_dados.html', 
            title='Ecommerce - Meus dados', 
            url = current_url, 
            user = current_user,
            usuario = usuario,
            form = form,
            categorias = categorias,
            total_itens = total_itens
        )
        
    flash('Você precisa estar logado para acessar esta área.')
    return redirect(url_for('index_user'))