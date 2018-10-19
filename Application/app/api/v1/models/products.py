# products models

from flask_restplus import Namespace, fields


api = Namespace('api/v1/products', description='Products related operations')

product = api.model('Product', {
    'product_id': fields.Integer(required=False, description='The product identifier'),
    'name': fields.String(required=True, description='The product name'),
    'price': fields.Integer(required=True, description='The product price'),
})


Products = []

product_update = api.model('Product updates',{
    'name': fields.String(required=True, description='The product name'),
    'price':fields.Integer(required=True, description='The product price'),

})
