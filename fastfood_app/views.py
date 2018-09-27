from fastfood_app import app
from flask import jsonify, abort, make_response, request
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
orders = [
    
    ]

@app.route('/FastFood/api/v1/orders', methods=['GET'])
def get_orders():
    if not orders:
        return make_response(jsonify({'message': 'There are no orders made'}), 404)
    return jsonify({'orders':orders}), 200

#This list stores the order available
item=[]

"""This function check whether the order id exists and if its an integer"""
def valid_order_id(order_id):
    if order_id.isdigit():
        return True
def available_orderid(order_id):
    if len(orders) > 0:
        for order in orders:
            if int(order['id']) == int(order_id):
                item.append(order)
        if item:
            return True


#This endpoint gets a specific order
@app.route('/FastFood/api/v1/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    # if not orders:
    #     return make_response(jsonify({'error': 'There are no orders currently'}), 404)
    if not valid_order_id(order_id):
        return make_response(jsonify({'Error': 'Invalid order id, order id should be an integer'}),400)
    elif  not available_orderid(order_id):
        return make_response(jsonify({'order':'That order has not yet been made'}),404)
    else:
        return jsonify({'order':item})
        
    
    

#Function for an endpoint to create new request
@app.route('/FastFood/api/v1/orders', methods=['POST'])
def place_order():
    if not request.json :
        return make_response(jsonify({'error_message': 'No parameters were passed'}), 404)
    elif not 'Food Name' in request.json:
        return make_response(jsonify({'error_message': 'Parameter Food Name missing'}), 404)
        
    elif not isinstance(request.json['Food Name'],str):
        bad_request = {
            "error": "Invalid order object",
            "help_string":
                "Request format should be {'category': 'Drinks or empty',"
                "'Food Name': 'orange juice','Description': 'Mixture of lemon and tangerine' }"
            }
        return jsonify({'bad_request':bad_request}), 400
    elif request.json['Food Name'].strip() == "":
        return make_response(jsonify({'error_message': 'Food Name valus cannot be empty'}), 404)

    else:
        if not orders:
            order = {
                    'id':1,
                    'category':request.json.get('category', ""),
                    'order status': False,
                    'Food Name':request.json['Food Name'],
                    'Description':request.json.get('Description', "")
                }
            orders.append(order)
            return jsonify({'order':order}), 201   
        else:
            order = {
                    'id':orders[-1]['id'] + 1,
                    'category':request.json.get('category', ""),
                    'order status': False,
                    'Food Name':request.json['Food Name'],
                    'Description':request.json.get('Description', "")
                }
            orders.append(order)
            return jsonify({'order':order}), 201
def invalid_order(order_request):
    if not order_request:
        return True
    if('category' in order_request and (type(order_request['category']) != str or order_request['category'].strip() == "")):
        return True
    if('order status' in order_request and (type(order_request['order status']) != str or order_request['order status'].strip() =="")):
        return True
    if('Food Name' in order_request and (type(request.json['Food Name']) != str or order_request['Food Name'].strip() == "")):
        return True
    if('Description' in request.json and (type(request.json['Description']) != str or order_request['Description'].strip() == "" or order_request['Description'].strip() == "")):
        return True


@app.route('/FastFood/api/v1/orders/<order_id>', methods=['PUT'])
@auth.login_required
def update_order_status(order_id):
    if not orders:
        return make_response(jsonify({'No orders': 'You cannot make any updates'}), 404)
    if invalid_order(request.json):
        return jsonify({'error': 'Invalid input or missing value'}), 404
    elif not valid_order_id(order_id):
        return jsonify({'Error': 'Invalid order id, order id should be an integer'}),400
    elif not available_orderid(order_id):
        return jsonify({'No order':'That order has not yet been made, no possible updates'}),404
    else:
        item[0]['category'] = request.json.get('category', item[0]['category'])
        item[0]['order status'] = request.json.get('order status', item[0]['order status'])
        item[0]['Food Name'] = request.json.get('Food Name', item[0]['Food Name'])
        item[0]['Description'] = request.json.get('Description', item[0]['Description'])
        return jsonify({'order':item[0]}), 200
        
    
    
    

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
    if not orders:
        return make_response(jsonify({'error': 'There are no orders'}), 404)
    else:
        id_orders = []
        for order in orders:
             if order['id'] == order_id:
                id_orders.append(order_id)
                orders.remove(order)
        if not id_orders:
            return make_response(jsonify({'error': 'That order does not exist'}), 404)
        return make_response(jsonify({'Message': 'order deleted'}), 200)