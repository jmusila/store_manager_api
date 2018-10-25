"""
    This is the products views, it has the endpoints related to products
    Authored by: Jonathan Musila
"""
from flask_restplus import Resource
from app.api.v1.models.products import Products, api, product, product_update
"""
Product List Class
Endpoints: GET all products, POST
"""
@api.route('/')
class ProductsList(Resource):
    @api.doc('list_products')
    @api.marshal_with(product, envelope='Products')
    def get(self):
        '''List all products'''
        return Products, 200
    """
    A method to add a product on the list
    :Param Name: A string the name of the product
    :Param Price: An Interger, the price
    """
    @api.expect(product, validate=True)
    def post(self):
        '''Post a product'''
        new_product = api.payload
        new_product['product_id'] = len(Products) + 1
        Products.append(new_product)
        return {'results': "Product added successfully", 'status': "ok"}, 201

"""
Product List Class
Endpoints: GET single, DELETE, UPDATE
"""
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
    """
    A method to update a product on the list
    :Param Name: A string the name of the product
    :Param Price: An Interger, the price
    :Id : Unique Identifier for the product
    """
    @api.doc('update_single_product')
    @api.expect(product_update)
    def put(self, id):
        '''Update a product given its identifier'''
        update = api.payload
        for product in Products:
            if product['product_id'] == id:
                product.update(update)
                return product, 201
            elif product['product_id'] != id:
                return {'Message':"Product with that id not found"}

        api.abort(404)
    """
    A method to delete a product on the list
    :Param Name: A string the name of the product
    :Param Price: An Interger, the price
    :Id : Unique Identifier for the product
    """
    def delete(self, id):
        for product in Products:
            if product['product_id'] == id:
                Products.remove(product)
                return {'results':"Product Deleted"}, 204
            elif product['product_id'] != id:
                return {'Message':"Product with that id not found"}