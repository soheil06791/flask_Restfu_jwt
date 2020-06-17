from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from flask_Restfu_jwt.database.model import Product


#productapi, getall and create product
class ProductsApi(Resource):
    @jwt_required
    def get(self):

        products = Product.objects().to_json()
        return Response(products, mimetype="application/json", status=200)
    @jwt_required
    def post(self):
        # user_id = get_jwt_identity()
        # user = User.objects.get(id=user_id)
        # added_by = user
        body = request.get_json(force=True)
        product = Product(**body, ).save()
        # user.update(push__products=product)
        # user.save()
        id = product.id
        return {'id': str(id)}, 200

#productapi, delete and update and single product by id product
class ProductApi(Resource):
    @jwt_required
    def put(self, id):
        user_id = get_jwt_identity()
        product = Product.objects.get(id=id, added_by=user_id)
        body = request.get_json(force=True)
        Product.objects.get(id=id).update(**body)
        return 'update', 200
    @jwt_required
    def delete(self, id):
        user_id = get_jwt_identity()
        product = Product.objects.get(id=id, added_by=user_id)
        product.delete()
        return '', 200
    @jwt_required
    def get(self, id):
        products = Product.objects.get(id=id).to_json()
        return Response(products, mimetype="application/json", status=200)