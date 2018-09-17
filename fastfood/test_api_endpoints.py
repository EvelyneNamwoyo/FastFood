import unittest
from fastfood_app import app
from fastfood_app import views
class EndpointTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        
    def tearDown(self):
        pass
    
    def test_to_get_all_orders(self):
        response = self.app.get('/FastFood/api/v2/orders')
        self.assertEqual(response.status_code, 200)
    

if __name__ == "__main__":
    unittest.main()