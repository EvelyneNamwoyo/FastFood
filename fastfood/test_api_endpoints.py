import unittest
from fastfood_app import app
from fastfood_app import views
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

    # def test_to fetch_order_with_nonexistant(self):
    #     response = self.app.get('/FastFood/api/v1/orders/9')
    #     self.assertEqual(response.status_code,404)

    def test_to_fetch_aspecific_order_when_nonexistant_is_ispassed(self):
        response = self.app.get('/FastFood/api/v1/orders/9')
        self.assertEqual(response.status_code,404)
        


    

if __name__ == "__main__":
    unittest.main()