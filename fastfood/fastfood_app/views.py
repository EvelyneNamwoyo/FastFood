from fastfood_app import app
from flask import jsonify, abort, make_response
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


@app.route('/FastFood/api/v1/orders', methods=['GET'])
def get_orders():
    return jsonify({'orders':orders})

#This endpoint gets a specific order
@app.route('/FastFood/api/v1/orders/<order_id>', methods=['GET'])
def get_order(order_id):

    # if (isinstance(order_id, int)): 
    #     b="int"
    # elif (isinstance(order_id, str)): 
    #     b="string"
    # # return type(order_id)
    # return jsonify({'type':b})
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


