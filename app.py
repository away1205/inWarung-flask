import os
from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_cors import CORS
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
CORS(app)

# WEBSITE_HOSTNAME exists only in production environment
if "WEBSITE_HOSTNAME" not in os.environ:
    # local development, where we'll use environment variables
    print("Loading config.development and environment variables from .env file.")
    app.config.from_object("azureproject.development")
else:
    # production
    print("Loading config.production.")
    app.config.from_object("azureproject.production")

app.config.update(
    SQLALCHEMY_DATABASE_URI=app.config.get("DATABASE_URI"),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# Initialize the DB connection
db.init_app(app)

# Enable Flask-Migrate commands "flask db init/migrate/upgrade" to work
migrate = Migrate(app, db)

# Define our api
api = Api(app)

# Set endpoints to get the data
api.add_resource(Users, "/api/users/")
api.add_resource(User, "/api/users/<string:id>")
api.add_resource(Products, "/api/products/")
api.add_resource(ProductResource, "/api/products/<string:id>")
api.add_resource(CategoryProducts, "/api/categories/")
api.add_resource(CategoryProductResource, "/api/categories/<string:id>")
api.add_resource(DetailTransactions, "/api/detail-transactions/")
api.add_resource(DetailTransactionResource, "/api/detail-transactions/<string:id>")
api.add_resource(Transactions, "/api/transactions/")
api.add_resource(TransactionResource, "/api/transactions/<string:id>")
api.add_resource(Restocks, "/api/restocks/")
api.add_resource(RestockResource, "/api/restocks/<string:id>")


@app.route("/")
def home():
    return "<h1>inWarung</h1>"


if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run(debug=False)
