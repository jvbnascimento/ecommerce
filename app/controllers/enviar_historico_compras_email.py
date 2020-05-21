from app import app

from flask import request, make_response

from app.controllers.enviar_email import enviarEmail

current_port = '8080/'

@app.route('/user/minhas_compras/email/<email>', methods=['GET', 'POST'])
def enviar_historico_compras_email(email):
    if request.method == "GET":
        pass
        # enviarEmail()

        # resposta = make_response(str(total_itens))
        # resposta.set_cookie('carrinho_compras', novoCookie)

        # return resposta