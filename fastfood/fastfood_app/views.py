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
       {
           'id': 3,
           'category': 'Drinks',
           'order status': False,
           'Food Name':'Mango Juice',
           'Description': 'Made from the natural african mango'}
    ]

@app.route('/FastFood/api/v1/orders', methods=['GET'])
def get_orders():
    if len(orders)==0:
        return make_response(jsonify({'message': 'There are no orders made'}), 404)

    return jsonify({'orders':orders}), 200

#This endpoint gets a specific order
@app.route('/FastFood/api/v1/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    if not order_id.isdigit():
        return jsonify({'Error': 'Invalid order id, order id should be an integer'}),400
    else:
        
        # order = [ order if order['id'] == order_id else 'That order has not yet been made' for order in orders ]
        if len(orders) > 0:
            item=[]
            for order in orders:
                if int(order['id']) == int(order_id):
                    item.append(order)
            if item == []:
                return jsonify({'order':'That order has not yet been made'}),404
            return jsonify({'order':item})
        
        else:
            return make_response(jsonify({'error': 'There are no orders currently'}), 404)

#Function for an endpoint to create new request
@app.route('/FastFood/api/v1/orders', methods=['POST'])
def place_order():
    if not request.json :
        return make_response(jsonify({'error_message': 'No parameters were passed'}), 404)
    elif not 'Food Name' in request.json:
        return make_response(jsonify({'error_message': 'Parameter Food Name missing'}), 404)
        
    elif not isinstance(request.json['Food Name'], str):
        bad_request = {
            "error": "Invalid order object",
            "help_string":
                "Request format should be {'category': 'Drinks or empty',"
                "'Food Name': 'orange juice','Description': 'Mixture of lemon and tangerine' }"
            }
        return jsonify({'bad_request':bad_request}), 400

    else:
        order = {
                'id':orders[-1]['id'] + 1,
                'category':request.json.get('category', ""),
                # 'category':request.json['category'],
                'order status': False,
                'Food Name':request.json['Food Name'],
                'Description':request.json.get('Description', "")
                # 'Description':request.json['Description']
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

@app.route('/FastFood/api/v1/orders/<int:order_id>', methods=['DELETE'])
@auth.login_required
def delete_order(order_id):
    if len(orders) == 0:
        return make_response(jsonify({'error': 'There are no orders currently'}), 404)
    else:
        id_orders = []
        for order in orders:
             if order['id'] == order_id:
                id_orders.append(order_id)
                orders.remove(order)
        if id_orders ==[]:
            return make_response(jsonify({'error': 'That order does not exist'}), 404)
        return make_response(jsonify({'Message': 'order deleted'}), 200)
        