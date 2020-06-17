from flask_mongoengine import MongoEngine

db = MongoEngine()

def init_db(app):
    return db.init_app(app)