from flask import Flask

from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.debug = True

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)

from app.models import usuario, produto, categoria, compra
from app.controllers import index, user, login, logout, cadastrar_usuario
from app.controllers import gerenciar_estoque, editar_produto, deletar_produto
from app.controllers import adicionar_carrinho, carrinho_compras
from app.controllers import remover_carrinho, gerenciar_cadastros
from app.controllers import editar_cadastro, deletar_cadastro, finalizar_compra
from app.controllers import minhas_compras