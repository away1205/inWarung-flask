from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    business_name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"User(username = {self.username}, email = {self.email}, business_name = {self.business_name})"


class Product(db.Model):
    id_product = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(80), nullable=False)
    id_category = db.Column(
        db.Integer, db.ForeignKey("category_product.id_category"), nullable=False
    )
    wholesale_price = db.Column(db.Float, nullable=False)
    retail_price = db.Column(db.Float, nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey("user_model.id"), nullable=False)

    def __repr__(self):
        return f"Product(name = {self.product_name}, wholesale_price = {self.wholesale_price}, retail_price = {self.retail_price})"


class CategoryProduct(db.Model):
    id_category = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("user_model.id"), nullable=False)
    category_name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"Category(name = {self.category_name})"


class DetailTransaction(db.Model):
    id_transaction = db.Column(
        db.Integer, db.ForeignKey("transaction.id_transaction"), primary_key=True
    )
    id_product = db.Column(
        db.Integer, db.ForeignKey("product.id_product"), primary_key=True
    )
    transaction_date = db.Column(db.DateTime, nullable=False)
    qty_purchases = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    price_subtotal = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"DetailTransaction(transaction_date = {self.transaction_date}, qty_purchases = {self.qty_purchases}, price = {self.price}, price_subtotal = {self.price_subtotal})"


class Transaction(db.Model):
    id_transaction = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("user_model.id"), nullable=False)

    def __repr__(self):
        return f"Transaction(id_transaction = {self.id_transaction}, id_user = {self.id_user})"


class Restock(db.Model):
    id_restock = db.Column(db.Integer, primary_key=True)
    restock_date = db.Column(db.DateTime, nullable=False)
    id_product = db.Column(
        db.Integer, db.ForeignKey("product.id_product"), nullable=False
    )
    qty_restock = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Restock(restock_date = {self.restock_date}, qty_restock = {self.qty_restock})"
