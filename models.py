from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = "user"

    id_user = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    business_name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"User(username = {self.username}, email = {self.email}, business_name = {self.business_name})"


class Product(db.Model):
    __tablename__ = "product"

    id_product = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(80), nullable=False)
    id_category = db.Column(
        db.Integer, db.ForeignKey("category_product.id_category"), nullable=False
    )
    wholesale_price = db.Column(db.Float, nullable=False)
    retail_price = db.Column(db.Float, nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey("user.id_user"), nullable=False)

    def __repr__(self):
        return f"Product(name = {self.product_name}, wholesale_price = {self.wholesale_price}, retail_price = {self.retail_price})"


class CategoryProduct(db.Model):
    __tablename__ = "category_product"

    id_category = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(80), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey("user.id_user"), nullable=False)

    def __repr__(self):
        return f"CategoryProduct(name = {self.category_name})"


class DetailTransaction(db.Model):
    __tablename__ = "detail_transaction"

    id_transaction = db.Column(db.Integer, primary_key=True)
    transaction_date = db.Column(db.DateTime, nullable=False)
    id_product = db.Column(
        db.Integer, db.ForeignKey("product.id_product"), nullable=False
    )
    qty_purchases = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    price_subtotal = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"DetailTransaction(date = {self.transaction_date}, product_id = {self.id_product}, qty = {self.qty_purchases}, price = {self.price}, subtotal = {self.price_subtotal})"


class Transaction(db.Model):
    __tablename__ = "transaction"

    id_transaction = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("user.id_user"), nullable=False)

    def __repr__(self):
        return f"Transaction(user_id = {self.id_user})"


class Restock(db.Model):
    __tablename__ = "restock"

    id_restock = db.Column(db.Integer, primary_key=True)
    restock_date = db.Column(db.DateTime, nullable=False)
    id_product = db.Column(
        db.Integer, db.ForeignKey("product.id_product"), nullable=False
    )
    qty_restock = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Restock(date = {self.restock_date}, product_id = {self.id_product}, qty = {self.qty_restock})"
