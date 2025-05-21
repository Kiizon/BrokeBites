import openai
import json
from typing import Dict, List

def generate_recipes(store_deals: Dict[str, List[Dict]]) -> List[Dict]:
    """
    Generate 3 simple recipes based on store deals' item names using OpenAI's API.
    Args:
        store_deals: Dictionary of store names to lists of deals (e.g., {'store': [{'item': str}, ...]})
    Returns:
        List of recipe dictionaries with title, ingredients, and instructions.
    """
    # Build a prompt listing each store's item names
    lines = []
    for store, deals in store_deals.items():
        lines.append(f"{store}:")
        for d in deals:
            item = d.get('item', 'Unknown Item')  # Use 'Unknown Item' if item is missing
            lines.append(f"- {item}")
        lines.append("")  # Blank line between stores

    # Prompt using only item names
    prompt = (
        "You are a helpful chef. Below are current grocery deals by store (item names only, including any provided measurements):\n\n"
        + "\n".join(lines)
        + "\n\nPlease suggest 3 simple recipes, each using 2-4 ingredients or more from the deals above. "
        "Each recipe must include only items from the provided list and can use items from any store. "
        "Ignore items that are not food (e.g., kitchenware). "
        "Normalize the ingredients to ensure clean, consistent data: include specific portion sizes or quantities for all ingredients, "
        "using the measurements provided in the deals when available (e.g., 'Raspberries 170 g') or adding reasonable quantities (e.g., '2 pieces' for Chicken Thighs, '1 cup' for rice) when not specified. "
        "Use standard culinary measurements (e.g., cups, tablespoons, pieces, grams) and avoid vague terms like 'some' or 'a handful'. "
        "Return the response as a JSON array of objects, where each object has the fields: "
        "'title' (string), 'ingredients' (array of strings, each including the item name and a specific portion size), and 'instructions' (string). "
        "Example format:\n"
        "[\n"
        "  {\"title\": \"Recipe Name\", \"ingredients\": [\"item1 1 cup\", \"item2 2 pieces\"], \"instructions\": \"Steps...\"},\n"
        "  ...\n"
        "]"
    )

    try:
        # Make OpenAI API call
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful chef who responds in JSON format."},
                {"role": "user", "content": prompt}
            ]
        )
        content = resp.choices[0].message.content

        # Handle potential markdown or non-JSON response
        try:
            # Remove markdown code blocks if present
            if content.startswith('```json'):
                content = content[7:-3].strip()  # Remove ```json and ```
            recipes = json.loads(content)
            if not isinstance(recipes, list):
                raise ValueError("OpenAI response is not a JSON array")
            return recipes
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            return [{"title": "Error", "ingredients": [], "instructions": "Failed to parse recipes from API response"}]
        except ValueError as e:
            print(f"Response format error: {e}")
            return [{"title": "Error", "ingredients": [], "instructions": "Invalid response format from API"}]

    except Exception as e:
        print(f"OpenAI API error: {e}")
        return [{"title": "Error", "ingredients": [], "instructions": "Failed to generate recipes due to API error"}]