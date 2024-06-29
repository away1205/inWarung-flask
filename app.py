from flask import Flask
from flask_restful import Api
from config import Config
from models import db
from resources import (
    Users,
    User,
    Products,
    ProductResource,
    CategoryProducts,
    CategoryProductResource,
    DetailTransactions,
    DetailTransactionResource,
    Transactions,
    TransactionResource,
    Restocks,
    RestockResource,
)

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the DB connection
db.init_app(app)

# Define our api
api = Api(app)

# Set endpoints to get the data
api.add_resource(Users, "/api/users/")
api.add_resource(User, "/api/users/<int:id>")
api.add_resource(Products, "/api/products/")
api.add_resource(ProductResource, "/api/products/<int:id>")
api.add_resource(CategoryProducts, "/api/categories/")
api.add_resource(CategoryProductResource, "/api/categories/<int:id>")
api.add_resource(DetailTransactions, "/api/detail-transactions/")
api.add_resource(DetailTransactionResource, "/api/detail-transactions/<int:id>")
api.add_resource(Transactions, "/api/transactions/")
api.add_resource(TransactionResource, "/api/transactions/<int:id>")
api.add_resource(Restocks, "/api/restocks/")
api.add_resource(RestockResource, "/api/restocks/<int:id>")


@app.route("/")
def home():
    return "<h1>Flask Rest Api</h1>"


if __name__ == "__main__":
    app.run(debug=True)
