"""
This module is users views

Authored by: Jonathan Musila
"""
import datetime
import re
import json
from flask import request
from flask_restplus import Resource, reqparse
from passlib.hash import pbkdf2_sha256 as sha256
from validate_email import validate_email
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

from app.api.v1.models.user import Users, api, user, user_login, api, UserModel

@api.route('/register')
class UserRegister(Resource):
    """
    A method to register a new user 
    Params: Firstname, Lastname, Password, Email
    """
    @api.expect(user, validate=True)
    def post(self):
        '''Post a sale'''
        data = request.get_json()
        new = api.payload
        new['user_id'] = len(Users) + 1
        firstname = data['firstname']
        email = data['email']
        raw_password = data['password']
        lastname = data['lastname']
        payload = ['user_id','password', 'email', 'lastname', 'firstname']

        email_format = re.compile(r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[.a-zA-Z-]+$)")

        if not email:
            return {'message': 'Email cannot be empty'}, 400
        elif not raw_password:
            return {'message': 'Password cannot be empty'}, 400
        elif not firstname:
            return {'message': 'Lastname cannot be empty'}, 400
        elif not lastname:
            return {'message': 'Lastname cannot be empty'}, 400
        elif len(raw_password) < 8:
            return {'message': 'Password should be at least 8 characters'}, 400
        elif not (re.match(email_format, email)):
            return {'message': 'Invalid email'}, 400
        else:
        # Check if the item is not required
            for item in data.keys():
                if item not in payload:
                    return {"message": "The field '{}' is not required for registration".format(item)}, 400

       

        password = raw_password

        # Try to send the registered user to the user model
        try:
            Users.append(new)
            return {
                'message': '{} was registered succesfully!'.format(email),
                'status': 'ok'
            }, 201

        except Exception as my_exception:
            print(my_exception)
            return {
                'message': 'Something went wrong'
            }, 500
    """
    A method to register all registered users
    """
    @api.doc('list_sales')
    @api.marshal_with(user, envelope='Users')
    def get(self):
        '''List all sales'''
        return Users, 200


@api.route('/login')
class UserLogin(Resource):
    """
    A method to login a user 
    Params:Password, Email
    """
    @api.expect(user_login, validate=True)
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']
        payload = ['password', 'email']
        current_user = UserModel.find_by_email(email)
        if password and email ==True:
                    
            access_token = create_access_token(identity = email, expires_delta=datetime.timedelta(hours=5))
            return {"access_token": access_token}, 200

        else:
            return {"results": "wrong credentials"}, 401
        


