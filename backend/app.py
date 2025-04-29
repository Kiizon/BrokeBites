from flask import Flask, request, jsonify
from flask_cors import CORS
from database import *
from scraper import *

app = Flask(__name__)
CORS(app)

# Get all current deals
@app.route('/deals', methods=['GET'])
def generate_recipes():
    deals = fetch_all_deals()
    deal_list = [
        {
            "item_name": item[0],
            "price": item[1],
            "store_name": item[2]
        }
        for item in deals
    ]
    return jsonify(deal_list)

# Get flyers by postal code (expects JSON with "postal_code")
@app.route('/api/flyers', methods=['POST'])
def get_flyers_route():
    data = request.get_json()
    postal_code = data.get("postal_code")

    flyers = fetch_flyer(postal_code)
    if flyers:
        flyer_list = [
            {
                "merchant": flyer["merchant"],
                "id": flyer["id"]
            }
            for flyer in flyers
        ]
        return jsonify(flyer_list)
    else:
        return jsonify({"error": "No flyers found"}), 404

# Get flyer items by flyer ID
@app.route('/api/flyers/<flyer_id>', methods=['GET'])
def get_flyer_for_store(flyer_id):
    flyer_data = fetch_flyer(flyer_id)
    if flyer_data:
        flyer_items = [
            {
                "name": item["name"],
                "price": item["price"]
            }
            for item in flyer_data
        ]
        return jsonify(flyer_items)
    else:
        return jsonify({"error": "No flyer data found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
