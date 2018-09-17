import unittest
from fastfood_app import views
class EndpointTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        # self.test_orders=[
        #                     {'id': 0,
        #                     'Category': 'Main Course',
        #                     'owner': 'Vernor Vinge',
        #                     'Food Name':'Chicken Stew',
        #                     'Description': 'Nice and tasty food'},
        #                     {'id': 2,
        #                     'Category': 'Main Course',
        #                     'owner': 'Erina Sis',
        #                     'Food Name':'Rice pilau',
        #                     'Description': 'Nice and tasty food'},
        #                     {'id': 3,
        #                     'Category': 'Drinks',
        #                     'owner': 'Sue Nalima',
        #                     'Food Name':'Mango Juice',
        #                     'Description': 'Made from the natural african mango'}
        #                 ]   
    def tearDown(self):
        pass
    
    def test_get_orders(self):
        response = self.app.get('/FastFood/api/v2/orders')
        self.assertEqual(response.status_code, 200)
