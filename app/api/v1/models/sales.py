# rcords models

from flask_restplus import Namespace, fields

api = Namespace('api/v1/sales', description='Sales related operations')

sale = api.model('Sales', {
    'sale_id': fields.Integer(required=False, description='The sale identifier'),
    'attendant': fields.String(required=True, description='The sale attendant'),
    'amount': fields.Integer(required=True, description='The total amount sold'),
    'items': fields.Integer(required=True, description='The total number of items sold'),
})


Sales = []