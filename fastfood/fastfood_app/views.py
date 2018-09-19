from fastfood_app import app
from flask import jsonify, make_response, request
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

#This endpoint gets a specific order
@app.route('/FastFood/api/v1/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = [ order for order in orders if order['id'] == order_id]
    if len(order) == 0:
        abort(404)
    return jsonify({'order':order[0]})

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



