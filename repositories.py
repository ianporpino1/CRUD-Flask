from models import db, User, Sale
from sqlalchemy import func

def add_user(user):
    db.session.add(user)
    db.session.commit()

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def get_user_id_from_email(email):
    user = User.query.filter_by(email=email).first()
    if user:
        return user.id
    else:
        None

def add_sale(sale):
    db.session.add(sale)
    db.session.commit()

def get_all_sales():
    return Sale.query.all()

def get_sale_by_id(sale_id):
    return Sale.query.get(sale_id)

def update_sale():
    db.session.commit()

def delete_sale(sale):
    db.session.delete(sale)
    db.session.commit()

def get_sales_by_period(start_date, end_date, user_id):
    return Sale.query.filter(Sale.user_id == user_id, Sale.data_venda >= start_date, Sale.data_venda <= end_date).all()

