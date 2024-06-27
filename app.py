from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from config import Config
from models import db
from resources import Users, User

app = Flask(__name__)
app.config.from_object(Config)

# initialize the DB connection
db.init_app(app)

# Define our api
api = Api(app)

# Set endpoints to get the data
api.add_resource(Users, '/api/users/')
api.add_resource(User, '/api/users/<int:id>')

@app.route('/')
def home():
    return '<h1>Flask Rest Api</h1>'

if __name__ == '__main__':
    app.run(debug=True)
