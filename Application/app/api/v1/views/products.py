from flask_restplus import Resource

from app.api.v1.models.products import Products, api, product, product_update


@api.route('/')
class ProductsList(Resource):
    @api.doc('list_products')
    @api.marshal_with(product, envelope='Products')
    def get(self):
        '''List all products'''
        return Products, 200

   