from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_wtf.file import FileRequired, FileAllowed

from app.models.usuario import Usuario

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    lembrar_me = BooleanField('Lembrar-me')
    acessar = SubmitField('Acessar')

class RegistrationForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmar_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    cadastrar = SubmitField('Cadastrar-se')

    def validar_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()

        if usuario is not None:
            raise ValidationError('Este email já está em uso. Escolha um email diferente e tente novamente.')

class CadastroProdutoForm(FlaskForm):
    descricao = StringField('Nome Produto', validators=[DataRequired()])
    quantidade = StringField('Quantidade', validators=[DataRequired()])
    preco = StringField('R$ Preço', validators=[DataRequired()])
    # imagem = FileField('Imagem', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Somente imagens!')])
    cadastrarProduto = SubmitField('Cadastrar Produto')