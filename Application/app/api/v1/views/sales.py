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


    @api.expect(sale, validate=True)
    def post(self):
        '''Post a sale'''
        new_sale = api.payload
        new_sale['sale_id'] = len(Sales) + 1
        Sales.append(new_sale)
        return {'results': "Sale added successfully"}, 201
