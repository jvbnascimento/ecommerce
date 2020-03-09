from app import db
from app import login

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Usuario(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), index=True, unique=True)
	nome = db.Column(db.String(64), index=True)
	senha_hash = db.Column(db.String(128))
	tipo = db.Column(db.Integer)
	compras = db.relationship('Compra', backref = 'compra', lazy = True)
	
	def __repr__(self):
		return '<Email {}>'.format(self.email)
		
	def set_senha(self, senha):
		self.senha_hash = generate_password_hash(senha)
		
	def check_senha(self, senha):
		return check_password_hash(self.senha_hash, senha)
		
	@login.user_loader
	def load_user(id):
		return Usuario.query.get(int(id))
