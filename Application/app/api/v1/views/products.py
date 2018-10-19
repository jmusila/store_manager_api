from flask_restplus import Resource

from app.api.v1.models.products import Products, api, product, product_update


@api.route('/')
class ProductsList(Resource):
    @api.doc('list_products')
    @api.marshal_with(product, envelope='Products')
    def get(self):
        '''List all products'''
        return Products, 200

    @api.expect(product, validate=True)
    def post(self):
        '''Post a product'''
        new_product = api.payload
        new_product['product_id'] = len(Products) + 1
        Products.append(new_product)
        return {'results': "Product added successfully", 'status': "ok"}, 201