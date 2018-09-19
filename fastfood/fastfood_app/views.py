from fastfood_app import app
from flask import jsonify,make_response
orders = [
        {
            'id': 1,
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
#This function gets all orders
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


