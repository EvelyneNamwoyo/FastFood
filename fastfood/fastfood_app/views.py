from fastfood_app import app
from flask import jsonify, abort, make_response, request
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
orders = [
    {
        'id': 1,
        'category': 'Main Course',
        'order status': False,
        'Food Name':'Chicken Stew',
        'Description': 'Nice and tasty food'},
    {
        'id': 2,
        'category': 'Main Course',
        'order status': False,
        'Food Name':'Rice pilau',
        'Description': 'Nice and tasty food'},

    {   'id': 3,
        'category': 'Drinks',
        'order status': False,
        'Food Name':'Mango Juice',
        'Description': 'Made from the natural african mango'}
]

@app.route('/FastFood/api/v2/orders', methods=['GET'])
def get_orders():
    return jsonify({'orders':orders})

#This endpoint gets a specific order
@app.route('/FastFood/api/v2/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = [ order for order in orders if order['id'] == order_id]
    if len(order) == 0:
        jsonify({'error': 'Not found'}), 404
    return jsonify({'order':order[0]})

#Function for an endpoint to create new request
@app.route('/FastFood/api/v2/orders', methods=['POST'])
def place_order():
    if not request.json or not 'Food Name' in request.json:
        abort(400)
    order = {
            'id':orders[-1]['id'] + 1,
            'category':request.json['category'],
            'order status': request.json['order status'],
            'Food Name':request.json['Food Name'],
            'Description':request.json['Description']
            }
    orders.append(order)
    return jsonify({'order':order}), 201


@app.route('/FastFood/api/v1/orders/<int:order_id>', methods=['PUT'])
@auth.login_required
def update_order_status(order_id):
    order = [ order for order in orders if order['id'] == order_id]
    if ((len(order)==0) or (not request.json) or ('category' in request.json and type(request.json['category']) != str) or ('order status' in request.json and type(request.json['order status']) != str) or ('Food Name' in request.json and type(request.json['Food Name']) != str) or ('Description' in request.json and type(request.json['Description']) != str)):
        jsonify({'error': 'Invalid innput'}), 404
    order[0]['category'] = request.json.get('category', order[0]['category'])
    order[0]['order status'] = request.json.get('order status', order[0]['order status'])
    order[0]['Food Name'] = request.json.get('Food Name', order[0]['Food Name'])
    order[0]['Description'] = request.json.get('Description', order[0]['Description'])
    return jsonify({'order':order[0]})

@auth.get_password
def get_password(username):
    if username=='admin':
        return 'Eva'
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'You need a user name to make order updates'}), 401)