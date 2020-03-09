from app import app

from flask import flash, request

from app.models.usuario import Usuario
from app.models.categoria import Categoria

current_port = '8080/'

@app.route('/adicionar_carrinho/produto/<id_produto>', methods=['GET', 'POST'])
def adicionar_carrinho(id_produto):
    current_url = request.url.split(current_port)
    current_url = current_url[1]

    return "id produto: " + str(id_produto)