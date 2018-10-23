"""
This module tests the products and sales resource thoroughly to ensure correct API functionality

Authored by: Jonathan Musila
"""

import unittest
import json

#local imports
from app import create_app

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()

        self.product = {
            "name":"Shirt", 
            "price":100
        }
        self.sale = {
            "attendant":"Jonathan",
	        "amount":2000,
	        "items":300
        }

   #test for get all products
    def test_get_all_products(self):
        res = self.client.post("/api/v1/products/", data=json.dumps(self.product), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res1 = self.client.get('/api/v1/products/')
        data = json.loads(res1.get_data().decode("UTF-8"))
        self.assertEqual(res1.status_code, 200)
        self.assertIn('Shirt', str(res1.data))

    #test get each product
    def test_get_each_product(self):
        """Test API can get a single product by using it's id."""
        rv = self.client.post('/api/v1/products/', data=json.dumps(self.product), content_type='application/json')
        self.assertEqual(rv.status_code, 201)
        rv = self.client.get("/api/v1/products/1")
        data = json.loads(rv.get_data().decode("UTF-8"))
        self.assertEqual(rv.status_code, 200)
        self.assertIn('Shirt', str(rv.data))
    #test update product details
    def test_update_product(self):
        """
        Test API can edit an existing product. (PUT request)

        """
        rv = self.client.post(
            '/api/v1/products/', content_type='application/json', data=json.dumps(self.product))
        self.assertEqual(rv.status_code, 201)
        rv = self.client.put(
            '/api/v1/products/1', content_type='application/json', data=json.dumps(self.product))
        self.assertEqual(rv.status_code, 201)
        results = self.client.get('/api/v1/products/1')
        self.assertIn('Shirt', str(results.data))
    #test
    def test_delete_product(self):
        """
        Test API can delete an existing product. (DELETE request).

        """
        rv = self.client.post(
            '/api/v1/products/', content_type='application/json', data=json.dumps(self.product))
        self.assertEqual(rv.status_code, 201)
        res = self.client.delete('/api/v1/products/1', content_type='application/json')
        self.assertEqual(res.status_code, 204)
        # Test to see if it exists, should return a 404
        result = self.client.get('/api/v1/products/1')
        self.assertEqual(result.status_code, 404)
        

    # test post product
    def test_post_product(self):
        res = self.client.post('api/v1/products', content_type='application/json', data=json.dumps(self.product))
        self.assertEqual(res.status_code, 201)

        def tearDown(self):
        """This function destroys all the variables
        that have been created during the test
        """
        del self.product
        del self.sale
    

if __name__ == '__main__':
    unittest.main()