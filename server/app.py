import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from services.flipp_persistence import store_flyers_and_deals  
from db import db, migrate
from services.region_data import get_store_deals_for_region
from services.gen_recipes import generate_recipes

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]        = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate.init_app(app, db)

from models.region import Region
from models.store  import Store
from models.deal   import Deal

@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Test route working"})

@app.route("/api/stores", methods=["POST"])
def stores():
    fsa   = request.json.get("postal_code","")[:3].upper()
    data  = get_store_deals_for_region(fsa)
    return jsonify(data)

@app.route("/api/recipes", methods=["POST"])
def recipes():
    try:
        # Expect JSON with a 'deals' key containing store_deals
        store_deals = request.json.get("deals", {})
        if not isinstance(store_deals, dict) or not store_deals:
            return jsonify({"error": "Invalid or empty deals data"}), 400
        
        recipes = generate_recipes(store_deals)
        return jsonify(recipes)
    except Exception as e:
        print(f"Endpoint error: {e}")
        return jsonify({"error": "Failed to generate recipes"}), 500



if __name__ == "__main__":
    app.run(debug=True, port=8000)
