import unittest
from flask import json,jsonify,request
from fastfood_app import app
from fastfood_app import views
class EndpointTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

        
    def tearDown(self):
        pass
    

    """This test functions checks whether the updated order was successful"""
    def test_to_update_status(self):
        response = self.app.put('/FastFood/api/v1/orders/2',data = json.dumps({"order status": "Ready"}), 
                                content_type="application/json", follow_redirects=True)
        self.assertEqual(response.status_code,200)

    """This test function checks whether status has not been updated incase no data was passed data"""
    def test_for_not_updated(self):
        response = self.app.put('/FastFood/api/v1/orders/2',data = json.dumps({}), 
                                content_type="application/json", follow_redirects=True)
        self.assertEqual(response.status_code,200)



if __name__ == "__main__":
    unittest.main()