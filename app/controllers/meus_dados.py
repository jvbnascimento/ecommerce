from app import app
from app import db

from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_required

from werkzeug.security import generate_password_hash, check_password_hash

from app.models.usuario import Usuario
from app.models.categoria import Categoria
from app.models.telefone import Telefone
from app.models.endereco import Endereco

from app.controllers.forms import EditarDadosUsuarioForm

from app.controllers.funcoes_extras import formatar_mostragem_cpf, formatar_mostragem_telefone, formatar_mostragem_endereco

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
        
        cpf_formatado = formatar_mostragem_cpf(usuario.cpf)
        telefone_formatado = formatar_mostragem_telefone(usuario.telefones[0].telefone)
        endereco_formatado = formatar_mostragem_endereco(usuario.enderecos[0].logradouro)

        estados = [
            "AC", "AL", "AP", "AM",
            "BA", "CE", "DF", "ES",
            "GO", "MA", "MT", "MS",
            "MG", "PA", "PB", "PR",
            "PE", "PI", "RJ", "RN",
            "RS", "RO", "RR", "SC",
            "SP", "SE", "TO"
        ]

        form = EditarDadosUsuarioForm()

        if form.validate_on_submit():
            if (form.nome.data == ""):
                flash("O campo NOME é obrigatório e não pode estar vazio.")
                return redirect(url_for('meus_dados'))
            elif (form.nascimento.data == ""):
                flash("O campo NASCIMENTO é obrigatório e não pode estar vazio.")
                return redirect(url_for('meus_dados'))
            elif (form.telefone.data == ""):
                flash("O campo TELEFONE é obrigatório e não pode estar vazio.")
                return redirect(url_for('meus_dados'))
            
            elif (form.cep.data == ""):
                flash("O campo CEP é obrigatório e não pode estar vazio.")
                return redirect(url_for('meus_dados'))
            elif (form.numero.data == ""):
                flash("O campo NÚMERO é obrigatório e não pode estar vazio.")
                return redirect(url_for('meus_dados'))
            
            elif (form.senha_atual.data != ""):
                nova_senha_criptografada = generate_password_hash(form.nova_senha.data)
                
                if (not check_password_hash(usuario.senha, form.senha_atual.data)):
                    flash("O campo SENHA_ATUAL não corresponde a sua senha.")
                    return redirect(url_for('meus_dados'))
                elif (form.nova_senha.data == ""):
                    flash("O campo NOVA_SENHA é obrigatório e não pode estar vazio.")
                    return redirect(url_for('meus_dados'))
                elif (form.confirmar_nova_senha.data == ""):
                    flash("O campo CONFIRMAR_NOVA_SENHA é obrigatório e não pode estar vazio.")
                    return redirect(url_for('meus_dados'))
                elif (not check_password_hash(nova_senha_criptografada, form.confirmar_nova_senha.data)):
                    flash("As NOVAS_SENHAS não correspondem. Verifique-as e tente novamente.")
                    return redirect(url_for('meus_dados'))
                
                usuario.senha = nova_senha_criptografada

            elif (
                form.senha_atual.data == "" and form.nova_senha.data != "" or
                form.senha_atual.data == "" and form.confirmar_nova_senha.data != ""
            ):
                flash("O campo SENHA_ATUAL é obrigatório e não pode estar vazio.")
                return redirect(url_for('meus_dados'))

            usuario.nome = form.nome.data
            usuario.nascimento = form.nascimento.data
            usuario.cpf = current_user.cpf
            usuario.email = form.email.data
            
            formatar_telefone = form.telefone.data
            novo_telefone = formatar_telefone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")

            usuario.telefones.append(
                Telefone(
                    telefone = novo_telefone
                )
            )

            usuario.enderecos.append(
                Endereco(
                    cep = form.cep.data,
                    logradouro = form.logradouro.data + ", Nº: " + form.numero.data,
                    complemento = form.complemento.data,
                    referencia = form.referencia.data,
                    bairro = form.bairro.data,
                    cidade = form.cidade.data,
                    estado = form.estado.data
                )
            )

            db.session.add(usuario)
            db.session.commit()

            if (usuario.senha == current_user.senha):
                flash('As alterações foram salvadas com sucesso.')
                return redirect(url_for('meus_dados'))
            else:
                flash('As alterações foram salvadas com sucesso.')
                return redirect(url_for('logout'))
        
        elif request.method == 'GET':
            form.nome.data = usuario.nome
            form.nascimento.data = usuario.nascimento
            form.telefone.data = telefone_formatado
            form.cpf.data = cpf_formatado

            form.email.data = usuario.email

            form.cep.data = usuario.enderecos[0].cep
            form.logradouro.data = endereco_formatado[0]
            form.numero.data = endereco_formatado[1]
            form.complemento.data = usuario.enderecos[0].complemento
            form.referencia.data = usuario.enderecos[0].referencia
            form.bairro.data = usuario.enderecos[0].bairro
            form.cidade.data = usuario.enderecos[0].cidade
            form.estado.data = usuario.enderecos[0].estado

        return render_template(
            'meus_dados.html',
            title='Ecommerce - Meus dados', 
            url = current_url, 
            user = current_user,
            usuario = usuario,
            form = form,
            categorias = categorias,
            total_itens = total_itens,
            estados = estados
        )
        
    flash('Você precisa estar logado para acessar esta área.')
    return redirect(url_for('index_user'))