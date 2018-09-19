from fastfood_app import app
from flask import jsonify, make_response
orders = [
        {
            'id': 0,
            'Category': 'Main Course',
            'order status': False,
            'Food Name':'Chicken Stew',
            'Description': 'Nice and tasty food'},
       {
           'id': 2,
           'Category': 'Main Course',
           'order status': False,
           'Food Name':'Rice pilau',
           'Description': 'Nice and tasty food'},
       {
           'id': 3,
           'Category': 'Drinks',
           'order status': False,
           'Food Name':'Mango Juice',
           'Description': 'Made from the natural african mango'}
    ]

@app.route('/FastFood/api/v1/orders', methods=['GET'])
def get_orders():
    if len(orders)==0:
        return make_response(jsonify({'message': 'There are no orders made'}), 404)

    return jsonify({'orders':orders}), 200

