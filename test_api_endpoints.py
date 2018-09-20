import unittest
from flask import json,jsonify,request
from fastfood_app import app
from fastfood_app import views
from base64 import b64encode
class EndpointTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

        
    def tearDown(self):
        pass
    
    def test_to_get_all_orders(self):
        response = self.app.get('/FastFood/api/v1/orders')
        self.assertEqual(response.status_code, 200)

    """These tests check for different status codes and responses for all possible order_id inputs"""    

    def test_to_fetch_aspecific_order(self):
        response = self.app.get('/FastFood/api/v1/orders/2')
        self.assertEqual(response.status_code,200)

    def test_to_throw_type_error_when_str_ispassed_as_id(self):
        order_id = "1"
        api_url = '/FastFood/api/v1/orders/'+ order_id
        response = self.app.get(api_url)
        self.assertRaises(TypeError, response)

    def test_to_fetch_order_when_str_ispassed_as_id(self):
        order_id = "1"
        api_url = '/FastFood/api/v1/orders/'+ order_id
        response = self.app.get(api_url)
        self.assertEqual(response.status_code, 404)

    def test_to_fetch_aspecific_order_when_nonexistant_is_ispassed(self):
        response = self.app.get('/FastFood/api/v1/orders/9')
        self.assertEqual(response.status_code,404)
        
    """This function checks whether api can make an order-post"""
    def test_to_place_order(self):
        response = self.app.post('/FastFood/api/v1/orders',data = json.dumps({"Food Name": "milk"}), 
                                content_type="application/json", follow_redirects=True)
        result = json.loads(response.data)
        self.assertEqual(result, {'order':{
                                'id':4,
                                'category': '',
                                'order status': False,
                                'Food Name':'milk',
                                'Description': ''
                                    }
                                })
        self.assertEqual(response.status_code,201)
    
    """This test function checks if mandatory parameter Food Name is not passed"""
    def test_for_mandatory_parameter_missing_in_placed_order(self):
        response = self.app.post('/FastFood/api/v1/orders',data = json.dumps({"Description": "Tasty food"}), 
                                content_type="application/json", follow_redirects=True)
        self.assertEqual(response.status_code,404)

    """This test function check whether Food Name parameter is a string"""
    def test_to_throw_type_error_when_str_is_notpassed_as_parameter(self):
        response = self.app.post('/FastFood/api/v1/orders',data = json.dumps({"Food Name": 4}), 
                                content_type="application/json", follow_redirects=True)
        self.assertRaises(TypeError, response)

    
    """This test functions checks whether the updated order was successful"""
    def test_to_update_status(self):
        
        headers = {
                   'Authorization': 'Basic %s' % b64encode(b"admin:Eva").decode("ascii")
                   }
        response = self.app.put('/FastFood/api/v1/orders/2',headers=headers, data = json.dumps({"order status": "Ready"}),
                                content_type="application/json", follow_redirects=True)
        self.assertEqual(response.status_code,200)

    """This test function checks whether status has not been updated incase no data was passed data"""
    def test_for_not_updated(self):
        headers = {
                   'Authorization': 'Basic %s' % b64encode(b"admin:Eva").decode("ascii")
                   }
        response = self.app.put('/FastFood/api/v1/orders/2',headers=headers, data = json.dumps({}),
                                content_type="application/json", follow_redirects=True)
        self.assertEqual(response.status_code,200)

    """This tests checks whether access denied message is returned for un authorized users"""
    def test_for_access_denied_for_unauthorized_users(self):
        response = self.app.put('/FastFood/api/v1/orders/1', data = json.dumps({}),
                                content_type="application/json", follow_redirects=True)
        self.assertEqual(response.status_code,401)

    def test_successful_delete(self):
        """This function tests whether an order was successfully deleted"""
        headers = {
                   'Authorization': 'Basic %s' % b64encode(b"admin:Eva").decode("ascii")
                   }
        response = self.app.delete('/FastFood/api/v1/orders/1',headers=headers)
        self.assertEqual(response.status_code,200)



if __name__ == "__main__":
    unittest.main()