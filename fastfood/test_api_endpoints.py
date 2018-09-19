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
        response = self.app.put('/FastFood/api/v1/orders/2', data = json.dumps({}),
                                content_type="application/json", follow_redirects=True)
        self.assertEqual(response.status_code,401)

    def test_successful_delete(self):
        """This function tests whether an order was successfully deleted"""
        headers = {
                   'Authorization': 'Basic %s' % b64encode(b"admin:Eva").decode("ascii")
                   }
        response = self.app.delete('/FastFood/api/v1/orders/3',headers=headers)
        self.assertEqual(response.status_code,200)



if __name__ == "__main__":
    unittest.main()