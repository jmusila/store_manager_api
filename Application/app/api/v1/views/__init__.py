#views/__init__.py

from flask_restplus import Api

from .products import api as product_api
from .sales import api as sale_api



api = Api(
    title ='Store-Manager',
    version='1.0',
    description='A simple store API',
)

api.add_namespace(product_api)
api.add_namespace(sale_api)
