[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/jonathanmusila/store_manager_api/blob/master/LICENSE)
[![Build Status](https://travis-ci.com/jonathanmusila/store_manager_api.svg?branch=master)](https://travis-ci.org/jonathanmusila/store_manager_api)
[![Coverage Status](https://coveralls.io/repos/github/joanathanmusila/store_manager_api/badge.svg?branch=master)](https://coveralls.io/github/jonathanmusila/store_manager_api?branch=master)
[![Code Climate](https://codeclimate.com/github/codeclimate/codeclimate/badges/gpa.svg)](https://codeclimate.com/github/jonathanmusila/store_manager_api)

## Store Manager

Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.


## Endpoints

| Endpoint       | Description          |   HTTP-verb  |
| ------------- |:-------------:| -----:| 
| /api/v1/products | Post a product | POST |
| /api/v1/sales  | Post a sale record      | POST   |
| /api/v1/products | Get all products |  GET |
| /api/v1/product/id | Get product by id | GET |
| /api/v1/sales | Get all sale records | GET |
| /api/v1/sales/id | Get a record by id | GET|
| /api/v1/products | Get all a product and update it |  PUT |
| /api/v1/products/id | Get product by id and delete it| DELETE |
| /api/v1/users/register | Post a user | POST |
| /api/v1/users/login | Post a login | POST|

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
A few requirements to install, run and test this project.

cd path/to/directory-your-directory
- git clone https://github.com/jonathanmusila/store_manager_api.git
 -Install virtual environment 
- cd to ride-my-way-api and execute the following commands:
    
    - $ virtualenv -p python3 env 
    - $ source env/bin/activate
    - $ pip install -r requirements.txt
    - $ pip install pytest
    
- To run tests, do:

    - $ pytests

- Then run the app by executing:
    - $ python3 run.py
    
- Install postman to test the various endpoints

## Testing
Manually open the index.html file in your preferred browser. Navigate through the pages with the links provided.

## Built With
* python

## Authors
Jonathan Musila