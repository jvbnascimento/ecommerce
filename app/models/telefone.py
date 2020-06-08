from app import db


class Telefone(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey('usuario.id'),
        nullable = False
    )
    telefone = db.Column(db.String(11))

    def __repr__(self):
	    return '<Telefone: {}>'.format(self.telefone)