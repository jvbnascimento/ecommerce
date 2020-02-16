from app import db


class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)

    def __repr__(self):
        return '<Nome {}>'.format(self.nome)

    def load_categoria(id):
        return Categoria.query.get(int(id))
