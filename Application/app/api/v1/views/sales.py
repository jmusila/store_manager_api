"""
This module is sales views

Authored by: Jonathan Musila
"""

from flask_restplus import Resource


from app.api.v1.models.sales import Sales, api, sale



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
