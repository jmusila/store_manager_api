"""
This module is users views

Authored by: Jonathan Musila
"""
from flask import request
from flask_restplus import Resource
from passlib.hash import pbkdf2_sha256 as sha256
from validate_email import validate_email
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

from app.api.v1.models.user import Users, api, user, user_login, api, UserModel

@api.route('/register')
class UserRegister(Resource):

    @api.expect(user, validate=True)
    def post(self):
        '''Post a sale'''
        
        data = request.get_json()
        new = api.payload
        id = len(Users) + 1
        firstname = data['firstname']
        email = data['email']
        password = UserModel.generate_hash(data['password'])
        lastname = data['lastname']

        new_user = {'user_id': id,
            'firstname': firstname,
            'email': email,
            'password':password,
            'lastname':lastname
        }
        try:
            Users.append(new_user)
            access_token = create_access_token(identity = data['email'])
            refresh_token = create_refresh_token(identity = data['email'])
            return {
                'message': 'User {} was created'.format(data['email']),
                'access_token': access_token,
                'refresh_token': refresh_token,
                "users":Users
                }, 200
        except:
            return {'message': 'Something went wrong'}, 500

    @api.doc('list_sales')
    @api.marshal_with(user, envelope='Users')
    def get(self):
        '''List all sales'''
        return Users, 200

@api.route('/login')
class UserLogin(Resource):
    @api.expect(user_login, validate=True)
    def post(self):
        data = request.get_json()
    
    
        for i in Users:
           
            if i['email'] == data['email']:
                
                if UserModel.verify_hash(data['password'], i['password']):
                    
                    access_token = create_access_token(identity = data['email'])
                    refresh_token = create_refresh_token(identity = data['email'])
                return {'access_token': access_token}, 200

            else:
                return {"results": "wrong credentials"}, 401
        


