from .prouducts import ProductApi, ProductsApi
from .authen import Signup,Login,Logout

def initialize_routes(api):
    api.add_resource(ProductsApi, '/api/products')
    api.add_resource(ProductApi, '/api/prouducts/<id>')
    api.add_resource(Signup, '/api/auth/signup')
    api.add_resource(Login, '/api/auth/login')
    api.add_resource(Logout, '/api/auth/logout')