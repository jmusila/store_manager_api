"""
This module is sales views

Authored by: Jonathan Musila
"""

from flask_restplus import Resource
from flask_jwt_extended import jwt_required

from app.api.v1.models.sales import Sales, api, sale

"""
A class for sale record operations
:Param Attendant: The name of the attendant 
posting the record
:Param Amount: An Interger, the amount sold
:Param Id : Unique Identifier for the product
:Param Items: The total items sold
"""
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

"""
A class to get a singel sale record on the list
:Param Attendant: The name of the attendant 
posting the record
:Param Amount: An Interger, the amount sold
:Param Id : Unique Identifier for the product
:Param Items: The total items sold
"""
@api.route('/<int:id>')
@api.param('id', 'The sale identifier')
@api.response(404, 'Sale not found')
class Record(Resource):
    @api.doc('get_single_sale')
    @api.marshal_with(sale)
    def get(self, id):
        '''Fetch a sale given its identifier'''
        for sale in Sales:
            if sale['sale_id'] == id:
                return sale, 200
        api.abort(404)
