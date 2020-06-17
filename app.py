from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngineSessionInterface
from flask_restful import Api

from database.db import db
from database.db import init_db

from flask_Restfu_jwt.resource.routes import initialize_routes

app = Flask(__name__)
app.config['JWT_SECRET_KEY']="44C176788A7EEF45F2F79F53D108F8FDC630B5A4B35D74097795CA35153C181C"
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

#jwt config
jwt = JWTManager(app)
#Restful and hash password config
api = Api(app)
bcrypt=Bcrypt(app)

#mongodb address and create db product
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/product'
}


app.session_interface = MongoEngineSessionInterface(db)
init_db(app)
initialize_routes(api)



