# products models
from flask_restplus import Namespace, fields, Resource
from passlib.hash import pbkdf2_sha256 as sha256
api = Namespace('api/v1/users/', description='Users related operations')

user = api.model('User', {
    'user_id': fields.Integer(required=False, description='The user identifier'),
    'firstname': fields.String(required=True, description='The user name'),
    'lastname': fields.String(required=True, description='The user lastname'),
    'email': fields.String(required=True, description='The user email'),
    'password': fields.String(required=True, description='The user password'),
})



Users = [        {
            "email": "tom@me.com",
            "lastname": "musila",
            "firstname": "Jonathan",
            "password": "$pbkdf2-sha256$29000$f.8doxTiPEfofU9JybnXWg$pfDt22GFnvKV0BQ5xALljR9Idux1dEFBBXcgN9hZdgQ",
            "user_id": 1
        }]

user_login = api.model('Login', {
    'email': fields.String(required=True, description='The user name'),
    'password': fields.String(required=True, description='The user email'),
    
})

class UserModel(Resource):
    ...
    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)