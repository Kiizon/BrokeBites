from flask import Flask, request, jsonify
from flask_cors import CORS
from database import *
from scrape_and_store import *
import os
import openai
from dotenv import load_dotenv
import json


load_dotenv()

app = Flask(__name__)
# Configure CORS to allow requests from the frontend
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:5173"],  # Vite's default port
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

openai.api_key = OPENAI_API_KEY

instructions = """

You are a frugal master chef. Given sale ingredients, curate 6 healthy meals including the title of the recipe, a brief description, portion sizes, a list of ingredients with measurements, step-by-step cooking instructions and a URL for a relevant image.

"""


def generate_recipes(items):
    prompt = f"""Given these sale items: {', '.join(items)}, generate 3 recipes that use these ingredients.
    For each recipe, provide:
    1. A title
    2. A brief description
    3. A list of ingredients with measurements
    4. Step-by-step cooking instructions
    5. A URL for a relevant image (use a food image API or placeholder)
    
    Format the response as a JSON array of recipes, where each recipe has:
    - id (number)
    - title (string)
    - description (string)
    - ingredients (array of strings)
    - instructions (array of strings)
    - image (string URL)
    """

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": "You are a helpful cooking assistant that generates recipes based on available ingredients."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

# Get all current deals
@app.route('/deals', methods=['GET'])
def get_deals():
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

    flyers = fetch_flyers(postal_code)
    if flyers:
        # Create a dictionary to store unique stores with their latest flyer ID
        unique_stores = {}
        for flyer in flyers:
            store = flyer["merchant"]
            # Only keep the first flyer ID for each store
            if store not in unique_stores:
                unique_stores[store] = flyer["id"]
        
        # Convert the dictionary to a list of store objects
        flyer_list = [
            {
                "merchant": store,
                "id": flyer_id
            }
            for store, flyer_id in unique_stores.items()
        ]
        return jsonify(flyer_list)
    else:
        return jsonify({"error": "No flyers found"}), 404

# Get flyer items by flyer ID
@app.route('/api/flyers/<flyer_id>', methods=['GET'])
def get_flyer_for_store(flyer_id):
    items = fetch_items(flyer_id)
    if items:
        return jsonify(items)
    else:
        return jsonify({"error": "No flyer data found"}), 404

# Generate recipes based on flyer items
@app.route('/api/flyers/<flyer_id>/recipes', methods=['GET'])
def get_recipes_for_flyer(flyer_id):
    try:
        items = fetch_items(flyer_id)
        
        if not items:
            return jsonify({"error": "No items found"}), 404

        # Extract item names for recipe generation
        item_names = [item["name"] for item in items]
        
        recipes_json = generate_recipes(item_names)
        print(f"Generated recipes JSON: {recipes_json}")  # Debug log
        
        # Parse the JSON string into a Python object
        try:
            recipes = json.loads(recipes_json)
            # Ensure we have an array of recipes
            if not isinstance(recipes, list):
                recipes = [recipes]
            print(f"Final recipes object: {recipes}")  # Debug log
            return jsonify(recipes)
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            # If JSON parsing fails, return a default recipe structure
            return jsonify([{
                "id": 1,
                "title": "Recipe with Available Ingredients",
                "description": f"Recipe using {', '.join(item_names)}",
                "ingredients": item_names,
                "instructions": ["Combine all ingredients and cook as desired."],
                "image": "https://via.placeholder.com/300x200?text=Recipe+Image"
            }])
    except Exception as e:
        print(f"Error in get_recipes_for_flyer: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
