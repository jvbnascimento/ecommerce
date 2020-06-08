from app import db
from app import login

from flask_login import UserMixin

class Usuario(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nome = db.Column(db.String(64), index = True)
	nascimento = db.Column(db.Date)
	cpf = db.Column(db.String(14))

	email = db.Column(db.String(120), index = True, unique = True)
	senha = db.Column(db.String(128))
	
	tipo = db.Column(db.Integer)

	compras = db.relationship('Compra', backref = 'usuario', lazy = True)
	enderecos = db.relationship('Endereco', backref = 'usuario', lazy = True)
	telefones = db.relationship('Telefone', backref = 'usuario', lazy = True)
	
	def __repr__(self):
		return '<Email {}>'.format(self.email)
		
	@login.user_loader
	def load_user(id):
		return Usuario.query.get(int(id))
