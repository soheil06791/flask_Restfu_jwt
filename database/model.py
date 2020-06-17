from .db import db
import datetime
from flask_bcrypt import check_password_hash,generate_password_hash


# product table
class Product(db.Document):
    name = db.StringField(required=True, unique=True)
    category = db.StringField()
    creation=db.DateTimeField(default=datetime.datetime.now())
    price = db.FloatField()


#user table and hash password and check password in login and relation to product table
class User(db.Document):
    username=db.StringField(required=True,unique=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True,min_length=6)
    products = db.ListField(db.ReferenceField('Product', reverse_delete_rule=db.PULL))

    def generate(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check(self,password):
        che=check_password_hash(self.password,password)
        return che

User.register_delete_rule(Product, 'added_by', db.CASCADE)



