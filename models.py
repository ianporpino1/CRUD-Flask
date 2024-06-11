from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    vendas = db.relationship('Sale', back_populates='usuario', cascade='all, delete-orphan')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_cliente = db.Column(db.String(50), nullable=False)
    produto = db.Column(db.String(80), nullable=False)
    valor = db.Column(db.Numeric(15,2), nullable=False)
    data_venda = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

    usuario = db.relationship('User', back_populates='vendas')

    def to_dict(self):
        return {
            'id': self.id,
            'nome_cliente': self.nome_cliente,
            'produto': self.produto,
            'valor': self.valor,
            'data_venda': self.data_venda.strftime('%d-%m-%Y')
        }