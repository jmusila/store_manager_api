from flask_restplus import Resource
from flask_jwt_extended import jwt_required
from app.api.v1.models.products import Products, api, product, product_update


@api.route('/')
class ProductsList(Resource):
    @api.doc('list_products')
    @api.marshal_with(product, envelope='Products')
    def get(self):
        '''List all products'''
        return Products, 200

    @jwt_required
    @api.expect(product, validate=True)
    def post(self):
        '''Post a product'''
        new_product = api.payload
        new_product['product_id'] = len(Products) + 1
        Products.append(new_product)
        return {'results': "Product added successfully", 'status': "ok"}, 201


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
    @jwt_required
    @api.doc('update_single_product')
    @api.expect(product_update)
    def put(self, id):
        '''Update a product given its identifier'''
        update = api.payload
        for product in Products:
            if product['product_id'] == id:
                product.update(update)
                return product, 201
        api.abort(404)
    @jwt_required
    def delete(self, id):
        for product in Products:
            if product['product_id'] == id:
                Products.remove(product)
                return {'results':"Product Deleted"}, 204