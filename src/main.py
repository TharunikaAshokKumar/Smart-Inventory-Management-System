# src/main.py
from flask import Flask, request, jsonify, render_template
from inventory import add_inventory_item, get_all_inventory_items, setup_database

app = Flask(__name__)

@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.json
    item = add_inventory_item(data['name'], data['category'], data['stock'], data['reorder'])
    return jsonify({"message": "Product added successfully!", "item": item.name})

@app.route('/inventory', methods=['GET'])
def inventory():
    items = get_all_inventory_items()
    return render_template('inventory.html', items=items)

@app.route('/predict_stock', methods=['POST'])
def predict_stock():
    data = request.json['data']
    # Dummy prediction logic
    for item in data:
        item['predicted_stock'] = item['current_stock'] - item['sales']
    return jsonify(data)

if __name__ == '__main__':
    setup_database()
    app.run(debug=True)

