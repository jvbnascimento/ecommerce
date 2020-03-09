from app import db


class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime)
    total_itens = db.Column(db.Integer)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable = False)

    def __repr__(self):
        return '<Compra {}>'.format(self.id)

    def load_categoria(id):
        return Categoria.query.get(int(id))