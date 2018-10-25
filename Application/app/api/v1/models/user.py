# products models
from flask_restplus import Namespace, fields, Resource
api = Namespace('api/v1/users/', description='Users related operations')

user = api.model('User', {
    'user_id': fields.Integer(required=False, description='The user identifier'),
    'firstname': fields.String(required=True, description='The user name'),
    'lastname': fields.String(required=True, description='The user lastname'),
    'email': fields.String(required=True, description='The user email'),
    'password': fields.String(required=True, description='The user password'),
})


Users = []

user_login = api.model('Login', {
    'email': fields.String(required=True, description='The user name'),
    'password': fields.String(required=True, description='The user email'),
    
})

