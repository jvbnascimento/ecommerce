from app import db


class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey('usuario.id'),
        nullable = False
    )
    logradouro = db.Column(db.String(120))
    complemento = db.Column(db.String(60))
    referencia = db.Column(db.String())
    bairro = db.Column(db.String(36))
    cidade = db.Column(db.String(36))
    estado = db.Column(db.String(2))
    cep = db.Column(db.String(9))

    def __repr__(self):
	    return '<Endereço: {}, Bairro: {}, CEP: {}, Cidade: {}, Estado: {}>'.format(self.logradouro, self.bairro, self.cep, self.cidade, self.estado)