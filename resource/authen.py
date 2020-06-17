import datetime
from flask import request
from flask_jwt_extended import create_access_token, get_raw_jwt, jwt_required, get_jwt_identity
from flask_restful import Resource

from blacklist import Blacklist

from flask_Restfu_jwt.database.model import User


# authentication all singup,login,logout
class Signup(Resource):

    def post(self):
        body = request.get_json(force=True)
        print(body)
        user = User(**body)
        user.generate()
        user.save()
        id = user.id
        return {'id': str(id)}, 200

class Login(Resource):

    def post(self):

        body = request.get_json(force=True)

        user=User.objects.get(username=body.get('username'))
        auth=user.check(body.get('password'))

        if not auth:
            return {'error': 'username or password invalid'}, 401

        expire=datetime.timedelta(minutes=5)
        accsess_token=create_access_token(identity=str(user.id))


        return {'token':accsess_token},200

class Logout(Resource):
    @jwt_required
    def post(self):
        jti=get_raw_jwt()['jti']
        user_id = get_jwt_identity()
        Blacklist.add(jti)
        return {'message':'logout succes!'}


