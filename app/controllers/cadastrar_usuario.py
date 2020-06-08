from app import app
from app import db

from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user

from werkzeug.security import generate_password_hash, check_password_hash

from app.controllers.forms import RegistrationForm

from app.models.usuario import Usuario
from app.models.endereco import Endereco
from app.models.telefone import Telefone
from app.models.categoria import Categoria

current_port = '8080/'

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_usuario():
    if current_user.is_authenticated:
        return redirect(url_for('index_user'))

    form = RegistrationForm()
    current_url = request.url.split(current_port)
    current_url = current_url[1]

    categorias = Categoria.query.order_by('nome').all()
    estados = [
        "AC", "AL", "AP", "AM",
        "BA", "CE", "DF", "ES",
        "GO", "MA", "MT", "MS",
        "MG", "PA", "PB", "PR",
        "PE", "PI", "RJ", "RN",
        "RS", "RO", "RR", "SC",
        "SP", "SE", "TO"
    ]

    if form.validate_on_submit():
        if (form.nome.data == ""):
            flash("O campo NOME é obrigatório e não pode estar vazio.")
            return redirect(url_for('cadastrar_usuario'))
        elif (form.nascimento.data == ""):
            flash("O campo NASCIMENTO é obrigatório e não pode estar vazio.")
            return redirect(url_for('cadastrar_usuario'))
        elif (form.telefone.data == ""):
            flash("O campo TELEFONE é obrigatório e não pode estar vazio.")
            return redirect(url_for('cadastrar_usuario'))
        elif (form.cpf.data == ""):
            flash("O campo CPF é obrigatório e não pode estar vazio.")
            return redirect(url_for('cadastrar_usuario'))
        
        elif (form.email.data == ""):
            flash("O campo EMAIL é obrigatório e não pode estar vazio.")
            return redirect(url_for('cadastrar_usuario'))
        elif (form.senha.data == ""):
            flash("O campo SENHA é obrigatório e não pode estar vazio.")
            return redirect(url_for('cadastrar_usuario'))
        elif (form.confirmar_senha.data == ""):
            flash("O campo CONFIRMAR_SENHA é obrigatório e não pode estar vazio.")
            return redirect(url_for('cadastrar_usuario'))
        elif (form.senha.data != form.confirmar_senha.data):
            flash("As SENHAS não correspondem. Verifique-as e tente novamente.")
            return redirect(url_for('cadastrar_usuario'))
        
        elif (form.cep.data == ""):
            flash("O campo CEP é obrigatório e não pode estar vazio.")
            return redirect(url_for('cadastrar_usuario'))
        elif (form.numero.data == ""):
            flash("O campo NÚMERO é obrigatório e não pode estar vazio.")
            return redirect(url_for('cadastrar_usuario'))

        usuario = Usuario(
            nome = form.nome.data,
            nascimento = form.nascimento.data,
            cpf = form.cpf.data,
            email = form.email.data,
            tipo = 2
        )
        senha_criptografada = generate_password_hash(form.senha.data)
        
        checar_senhas_confirmam = check_password_hash(senha_criptografada, form.confirmar_senha.data)

        if (checar_senhas_confirmam):
            usuario.senha = senha_criptografada
        else:
            flash("As SENHAS não correspondem. Verifique-as e tente novamente.")
            return redirect(url_for('cadastrar_usuario'))
        
        # FORMATAR TELEFONE
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

        flash('Parabéns, seu cadastro foi concluído com êxito!')
        return redirect(url_for('login'))

    return render_template(
        'cadastro_usuario.html', 
        title = 'Ecommerce - Cadastre-se', 
        form = form, 
        url = current_url,
        categorias = categorias,
        estados = estados
    )