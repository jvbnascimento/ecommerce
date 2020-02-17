from app import db

produto_categoria = db.Table('produto_categoria',
                             db.Column('produto_id', db.Integer, db.ForeignKey(
                                 'produto.id'), primary_key=True),
                             db.Column('categoria_id', db.Integer, db.ForeignKey(
                                 'categoria.id'), primary_key=True),
                             )


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String)
    quantidade = db.Column(db.Integer)
    preco = db.Column(db.Float)
    imagem = db.Column(db.String)
    categorias_produto = db.relationship(
        'Categoria', secondary=produto_categoria, backref=db.backref('produtos', lazy=True))

    def __repr__(self):
        return '<Descricao:{}, Quantidade:{}, Preco:{}, Imagem:{}>'.format(self.descricao, self.quantidade, self.preco, self.imagem)

    def load_produto(id):
        return Produto.query.get(int(id))
