from app import db


class CompraProduto(db.Model):
    compra_id = db.Column(
        'compra_id',
        db.Integer,
        db.ForeignKey('compra.id'),
        primary_key=True
    )
    produto_id = db.Column(
        'produto_id',
        db.Integer,
        db.ForeignKey('produto.id'),
        primary_key=True
    )
    quantidade_item = db.Column('quantidade_item', db.Integer)
    preco_item = db.Column('preco_item', db.Float)
    produto = db.relationship("Produto")


class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime)
    total_itens = db.Column(db.Integer)
    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey('usuario.id'),
        nullable=False
    )
    produtos_compra = db.relationship('CompraProduto')

    def __repr__(self):
        return '<Compra {}>'.format(self.id)
