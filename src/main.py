from flask import Flask, request, jsonify
from inventory import add_product, get_inventory
from ai_model import predict_stock_level

app = Flask(__name__)

@app.route('/add_product', methods=['POST'])
def add_product_route():
    data = request.json
    add_product(data['name'], data['category'], data['stock'], data['reorder'])
    return jsonify({"message": "Product added successfully"}), 201

@app.route('/inventory', methods=['GET'])
def inventory_route():
    inventory = get_inventory()
    return jsonify([product.__dict__ for product in inventory])

@app.route('/predict_stock', methods=['POST'])
def predict_stock_route():
    data = request.json['data']
    predictions = predict_stock_level(data)
    return jsonify({"predictions": predictions})

if __name__ == '__main__':
    app.run(debug=True)

