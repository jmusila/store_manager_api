from flask_restplus import Resource

from app.api.v1.models.products import Products, api, product, product_update





@api.route('/<int:id>')
#@api.param('id', 'The product identifier')
@api.response(404, 'Product not found')
class Product(Resource):
    @api.doc('get_single_product')
    @api.marshal_with(product)
    def get(self, id):
        '''Fetch a product given its identifier'''
        for product in Products:
            if product['product_id'] == id:
                return product, 200
        api.abort(404)

    