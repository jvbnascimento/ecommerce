#IMPORTACAO DE PACOTES
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def enviarEmail(self, novaMensagem, novoEmail, novaSenha, novoDestinatario, novoAssunto):
    # CRIANDO A INSTANCIA DO OBJETO msg
    msg = MIMEMultipart()

    # MENSAGEM A SER ENVIADA
    mensagem = novaMensagem

    # PARAMETROS DA CONTA
    senha = novaSenha
    msg['From'] = novoEmail
    msg['To'] = novoDestinatario
    msg['Subject'] = novoAssunto

    # ADICIONAR MENSAGEM NO CORPO DO EMAIL
    msg.attach(MIMEText(mensagem, 'plain'))

    # CRIANDO SERVIDOR
    servidor = smtplib.SMTP('smtp.gmail.com: 587')
    servidor.starttls()

    # FAZER LOGIN NO EMAIL COM AS CREDENCIAIS
    servidor.login(msg['From'], senha)

    # ENVIAR A MENSAGEM PELO SERVIDOR
    try:
        servidor.sendmail(msg['From'], msg['To'], msg.as_string())
        servidor.quit()

        return 200
    except Exception as e:
        return e