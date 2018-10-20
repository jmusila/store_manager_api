"""
This module is sales views

Authored by: Jonathan Musila
"""

from flask_restplus import Resource


from app.api.v1.models.sales import Sales, api, sale

# class for sale list operations
@api.route('/')
class SalesList(Resource):
    @api.doc('list_sales')
    @api.marshal_with(sale, envelope='Sales')
    def get(self):
        '''List all sales'''
        return Sales, 200



