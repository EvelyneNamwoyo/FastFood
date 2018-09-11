from fastfood_app import app
orders = [
    {'id': 0,
     'Category': 'Main Course',
     'owner': 'Vernor Vinge',
     'Food Name':'Chicken Stew',
     'Description': 'Nice and tasty food'
     },
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

@app.route('/orders', methods=['GET'])
def get_orders():
