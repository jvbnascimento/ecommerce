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

from app.controllers import index, user, login, logout, cadastrar_usuario, gerenciar_estoque, editar_produto, deletar_produto, fazer_compra, adicionar_carrinho
from app.models import usuario, produto, categoria, compra