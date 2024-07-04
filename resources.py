from flask_restful import Resource, reqparse, fields, marshal_with, abort
from models import (
    db,
    UserModel,
    Product,
    CategoryProduct,
    DetailTransaction,
    Transaction,
    Restock,
)

# Fields for marshalling the data
userFields = {
    "id_user": fields.String,
    "email": fields.String,
    "username": fields.String,
    "business_name": fields.String,
}

productFields = {
    "id_product": fields.String,
    "product_name": fields.String,
    "id_category": fields.String,
    "current_stock": fields.Integer,
    "wholesale_price": fields.Float,
    "retail_price": fields.Float,
    "id_user": fields.Integer,
}

categoryProductFields = {
    "id_category": fields.String,
    "id_user": fields.String,
    "category_name": fields.String,
}

detailTransactionFields = {
    "id_transaction": fields.String,
    "id_detail_transaction": fields.String,
    "transaction_date": fields.DateTime,
    "id_product": fields.Integer,
    "qty_purchases": fields.Integer,
    "price": fields.Float,
    "price_subtotal": fields.Float,
}

transactionFields = {"id_transaction": fields.String, "id_user": fields.String}

restockFields = {
    "id_restock": fields.String,
    "restock_date": fields.DateTime,
    "id_product": fields.String,
    "qty_restock": fields.Integer,
}

# Parsers for the request arguments
user_args = reqparse.RequestParser()

user_args.add_argument("email", type=str, required=True, help="Email cannot be blank")
user_args.add_argument("id_user", type=str, required=True, help="id user cannot be blank")
user_args.add_argument(
    "username", type=str, required=True, help="Username cannot be blank"
)
user_args.add_argument(
    "business_name", type=str, required=True, help="Business name cannot be blank"
)

product_args = reqparse.RequestParser()
product_args.add_argument(
    "product_name", type=str, required=True, help="Product name cannot be blank"
)
product_args.add_argument(
    "id_category", type=str, required=True, help="Category ID cannot be blank"
)
product_args.add_argument(
    "id_product", type=str, required=True, help="Product ID cannot be blank"
)
product_args.add_argument(
    "wholesale_price", type=float, required=True, help="Wholesale price cannot be blank"
)
product_args.add_argument(
    "retail_price", type=float, required=True, help="Retail price cannot be blank"
)
product_args.add_argument(
    "current_stock", type=int, required=True, help="current stock cannot be blank"
)
product_args.add_argument(
    "id_user", type=str, required=True, help="User ID cannot be blank"
)

category_product_args = reqparse.RequestParser()
category_product_args.add_argument(
    "id_user", type=str, required=True, help="User ID cannot be blank"
)
category_product_args.add_argument(
    "category_name", type=str, required=True, help="Category name cannot be blank"
)
category_product_args.add_argument(
    "id_category", type=str, required=True, help="Category ID cannot be blank"
)

detail_transaction_args = reqparse.RequestParser()
detail_transaction_args.add_argument(
    "id_transaction", type=str, required=True, help="Transaction ID cannot be blank"
)
detail_transaction_args.add_argument(
    "id_detail_transaction", type=str, required=True, help="Detail Transaction ID cannot be blank"
)
detail_transaction_args.add_argument(
    "transaction_date", type=str, required=True, help="Transaction date cannot be blank"
)
detail_transaction_args.add_argument(
    "id_product", type=str, required=True, help="Product ID cannot be blank"
)
detail_transaction_args.add_argument(
    "qty_purchases", type=int, required=True, help="Quantity purchases cannot be blank"
)
detail_transaction_args.add_argument(
    "price", type=float, required=True, help="Price cannot be blank"
)
detail_transaction_args.add_argument(
    "price_subtotal", type=float, required=True, help="Price subtotal cannot be blank"
)

transaction_args = reqparse.RequestParser()
transaction_args.add_argument(
    "id_user", type=str, required=True, help="User ID cannot be blank"
)
transaction_args.add_argument(
    "id_transaction", type=str, required=True, help="Transaction ID cannot be blank"
)

restock_args = reqparse.RequestParser()
restock_args.add_argument(
    "restock_date", type=str, required=True, help="Restock date cannot be blank"
)
restock_args.add_argument(
    "id_product", type=str, required=True, help="Product ID cannot be blank"
)
restock_args.add_argument(
    "qty_restock", type=int, required=True, help="Quantity restock cannot be blank"
)


class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users

    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(
            id_user=args["id_user"],
            email=args["email"],
            username=args["username"],
            business_name=args["business_name"],
        )
        db.session.add(user)
        db.session.commit()
        return user, 201


class User(Resource):
    @marshal_with(userFields)
    def get(self, id):
        user = UserModel.query.filter_by(id_user=id).first()
        if not user:
            abort(404, message="User not found")
        return user

    @marshal_with(userFields)
    def patch(self, id):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(id_user=id).first()
        if not user:
            abort(404, message="User not found")
        user.email = args["email"]
        user.username = args["username"]
        user.business_name = args["business_name"]
        db.session.commit()
        return user

    @marshal_with(userFields)
    def delete(self, id):
        user = UserModel.query.filter_by(id_user=id).first()
        if not user:
            abort(404, message="User not found")
        db.session.delete(user)
        db.session.commit()
        return "", 204


class Products(Resource):
    @marshal_with(productFields)
    def get(self):
        products = Product.query.all()
        return products

    @marshal_with(productFields)
    def post(self):
        args = product_args.parse_args()
        product = Product(
            id_product=args["id_product"],
            id_category=args["id_category"],
            id_user=args["id_user"],
            current_stock=args["current_stock"],
            product_name=args["product_name"],
            wholesale_price=args["wholesale_price"],
            retail_price=args["retail_price"],
        )
        db.session.add(product)
        db.session.commit()
        return product, 201


class ProductResource(Resource):
    @marshal_with(productFields)
    def get(self, id):
        product = Product.query.filter_by(id_product=id).first()
        if not product:
            abort(404, message="Product not found")
        return product

    @marshal_with(productFields)
    def patch(self, id):
        args = product_args.parse_args()
        product = Product.query.filter_by(id_product=id).first()
        if not product:
            abort(404, message="Product not found")
        product.product_name = args["product_name"]
        product.id_category = args["id_category"]
        product.wholesale_price = args["wholesale_price"]
        product.retail_price = args["retail_price"]
        product.id_user = args["id_user"]
        db.session.commit()
        return product

    @marshal_with(productFields)
    def delete(self, id):
        product = Product.query.filter_by(id_product=id).first()
        if not product:
            abort(404, message="Product not found")
        db.session.delete(product)
        db.session.commit()
        return "", 204


class CategoryProducts(Resource):
    @marshal_with(categoryProductFields)
    def get(self):
        categories = CategoryProduct.query.all()
        return categories

    @marshal_with(categoryProductFields)
    def post(self):
        args = category_product_args.parse_args()
        category = CategoryProduct(
            id_user=args["id_user"], category_name=args["category_name"], id_category=args["id_category"],
        )
        db.session.add(category)
        db.session.commit()
        return category, 201


class CategoryProductResource(Resource):
    @marshal_with(categoryProductFields)
    def get(self, id):
        category = CategoryProduct.query.filter_by(id_category=id).first()
        if not category:
            abort(404, message="Category not found")
        return category

    @marshal_with(categoryProductFields)
    def patch(self, id):
        args = category_product_args.parse_args()
        category = CategoryProduct.query.filter_by(id_category=id).first()
        if not category:
            abort(404, message="Category not found")
        category.id_user = args["id_user"]
        category.category_name = args["category_name"]
        db.session.commit()
        return category

    @marshal_with(categoryProductFields)
    def delete(self, id):
        category = CategoryProduct.query.filter_by(id_category=id).first()
        if not category:
            abort(404, message="Category not found")
        db.session.delete(category)
        db.session.commit()
        return "", 204


class DetailTransactions(Resource):
    @marshal_with(detailTransactionFields)
    def get(self):
        details = DetailTransaction.query.all()
        return details

    @marshal_with(detailTransactionFields)
    def post(self):
        args = detail_transaction_args.parse_args()
        detail = DetailTransaction(
            id_detail_transaction=args["id_detail_transaction"],
            id_transaction=args["id_transaction"],
            transaction_date=args["transaction_date"],
            id_product=args["id_product"],
            qty_purchases=args["qty_purchases"],
            price=args["price"],
            price_subtotal=args["price_subtotal"],
        )
        db.session.add(detail)
        db.session.commit()
        return detail, 201


class DetailTransactionResource(Resource):
    @marshal_with(detailTransactionFields)
    def get(self, id):
        detail = DetailTransaction.query.filter_by(id_transaction=id).first()
        if not detail:
            abort(404, message="Detail transaction not found")
        return detail

    @marshal_with(detailTransactionFields)
    def patch(self, id):
        args = detail_transaction_args.parse_args()
        detail = DetailTransaction.query.filter_by(id_transaction=id).first()
        if not detail:
            abort(404, message="Detail transaction not found")
        detail.transaction_date = args["transaction_date"]
        detail.id_product = args["id_product"]
        detail.qty_purchases = args["qty_purchases"]
        detail.price = args["price"]
        detail.price_subtotal = args["price_subtotal"]
        db.session.commit()
        return detail

    @marshal_with(detailTransactionFields)
    def delete(self, id):
        detail = DetailTransaction.query.filter_by(id_transaction=id).first()
        if not detail:
            abort(404, message="Detail transaction not found")
        db.session.delete(detail)
        db.session.commit()
        return "", 204


class Transactions(Resource):
    @marshal_with(transactionFields)
    def get(self):
        transactions = Transaction.query.all()
        return transactions

    @marshal_with(transactionFields)
    def post(self):
        args = transaction_args.parse_args()
        transaction = Transaction(id_user=args["id_user"], id_transaction=args["id_transaction"])
        db.session.add(transaction)
        db.session.commit()
        return transaction, 201


class TransactionResource(Resource):
    @marshal_with(transactionFields)
    def get(self, id):
        transaction = Transaction.query.filter_by(id_transaction=id).first()
        if not transaction:
            abort(404, message="Transaction not found")
        return transaction

    @marshal_with(transactionFields)
    def patch(self, id):
        args = transaction_args.parse_args()
        transaction = Transaction.query.filter_by(id_transaction=id).first()
        if not transaction:
            abort(404, message="Transaction not found")
        transaction.id_user = args["id_user"]
        db.session.commit()
        return transaction

    @marshal_with(transactionFields)
    def delete(self, id):
        transaction = Transaction.query.filter_by(id_transaction=id).first()
        if not transaction:
            abort(404, message="Transaction not found")
        db.session.delete(transaction)
        db.session.commit()
        return "", 204


class Restocks(Resource):
    @marshal_with(restockFields)
    def get(self):
        restocks = Restock.query.all()
        return restocks

    @marshal_with(restockFields)
    def post(self):
        args = restock_args.parse_args()
        restock = Restock(
            restock_date=args["restock_date"],
            id_restock=args["id_restock"],
            id_product=args["id_product"],
            qty_restock=args["qty_restock"],
        )
        db.session.add(restock)
        db.session.commit()
        return restock, 201


class RestockResource(Resource):
    @marshal_with(restockFields)
    def get(self, id):
        restock = Restock.query.filter_by(id_restock=id).first()
        if not restock:
            abort(404, message="Restock not found")
        return restock

    @marshal_with(restockFields)
    def patch(self, id):
        args = restock_args.parse_args()
        restock = Restock.query.filter_by(id_restock=id).first()
        if not restock:
            abort(404, message="Restock not found")
        restock.restock_date = args["restock_date"]
        restock.id_product = args["id_product"]
        restock.qty_restock = args["qty_restock"]
        db.session.commit()
        return restock

    @marshal_with(restockFields)
    def delete(self, id):
        restock = Restock.query.filter_by(id_restock=id).first()
        if not restock:
            abort(404, message="Restock not found")
        db.session.delete(restock)
        db.session.commit()
        return "", 204
