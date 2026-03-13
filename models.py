from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(200), nullable=False)


class Order(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    product_name = db.Column(db.String(100))

    price = db.Column(db.Integer)

    quantity = db.Column(db.Integer)

    total_price = db.Column(db.Integer)