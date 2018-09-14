from fastfood_app import app
from flask import jsonify, abort, make_response, request
orders = [
    {'id': 0,
     'Category': 'Main Course',
     'owner': 'Vernor Vinge',
     'Food Name':'Chicken Stew',
     'Description': 'Nice and tasty food'},
    {'id': 2,
     'Category': 'Main Course',
     'owner': 'Erina Sis',
     'Food Name':'Rice pilau',
     'Description': 'Nice and tasty food'},
    {'id': 3,
     'Category': 'Drinks',
     'owner': 'Sue Nalima',
     'Food Name':'Mango Juice',
     'Description': 'Made from the natural african mango'}
]
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/FastFood/api/v2/orders', methods=['GET'])
def get_orders():
    return jsonify({'orders':orders})

#This endpoint gets a specific order
@app.route('/FastFood/api/v2/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = [ order for order in orders if order['id'] == order_id]
    if len(order) == 0:
        abort(404)
    return jsonify({'order':order[0]})

#Function for an endpoint to create new request
@app.route('/FastFood/api/v2/orders', methods=['POST'])
def place_order():
    if not request.json or not 'Food Name' in request.json:
        abort(400)
    order = {
            'id':orders[-1]['id'] + 1,
            'category':request.json['category'],
            'owner': request.json['owner'],
            'Food Name':request.json['Food Name'],
            'Description':request.json['Description']
            }
    orders.append(order)
    return jsonify({'order':order}), 201


@app.route('/FastFood/api/v2/orders/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):
    order = [ order for order in orders if order['id'] == order_id]
    if ((len(order)==0) or (not request.json) or ('category' in request.json and type(request.json['category']) != unicode) or ('owner' in request.json and type(request.json['owner']) != unicode) or ('Food Name' in request.json and type(request.json['Food Name']) != unicode) or ('Description' in request.json and type(request.json['Description']) != unicode)):
        abort(400)
    order[0]['category'] = request.json.get('category', order[0]['category'])
    order[0]['owner'] = request.json.get('owner', order[0]['owner'])
    order[0]['Food Name'] = request.json.get('Food Name', order[0]['Food Name'])
    order[0]['Description'] = request.json.get('Description', order[0]['Description'])
    return jsonify({'order':order[0]})