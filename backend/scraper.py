import requests 
import random
from database import insert_deal, clear_deals

FLYER_URL = "https://flyers-ng.flippback.com/api/flipp/flyers/7238751/flyer_items?locale=en"
STORE_NAME = "No Frills"

GROCERY_STORES = {"No Frills", "Walmart", "Metro"}

def generate_sid():
  return ''.join([str(random.randint(0, 9)) for _ in range(16)])

def fetch_all_flyers(postal_code):
  print("Fetching flyer data from postal code...")
  sid = generate_sid()
  URL = f"https://flyers-ng.flippback.com/api/flipp/data?locale=en&postal_code={postal_code}&sid={sid}"

  headers = {
    "User-Agent" : "Mozilla/5.0"
  }

  response = requests.get(URL, headers=headers)
  if response.status_code == 200:
    return response.json()
  else:
    print(f"Failed to fetch data from postal code: {response.status_code}")
    return None
  
  data = response.json()

  # filter flyer merchant and flyer id
  grocery_flyers = []
  for flyer in data.get("flyers", []):
    flyer_merchant = flyer.get("merchant", "Unknown merhchant")
    flyer_id = flyer.get("id", "Unknown ID")
    
    # filter to only stores in GROCERY_STORES
    if any(store in GROCERY_STORES for store in flyer_stores):
      grocery_flyers.append({
        "mechant": flyer_merchant,
        "id": flyer_id,
      })
    
    return grocery_flyers

  
def fetch_flyer(flyer_id):
  print("Fetching flyer data...")
  FLYER_URL = f"https://flyers-ng.flippback.com/api/flipp/flyers/{flyer_id}/flyer_items?locale=en"

  response = requests.get(FLYER_URL)
  if response.status_code == 200:
    return response.json()
  else:
    print(f"Failed to fetch flyer data: {response.status_code}")
    return None
  
  data = response.json()

  clear_deals()


def scrape_flyer():
  print("Scraping flyer data...")
  response = requests.get(FLYER_URL)
  if response.status_code != 200:
    print(f" Failed to fetch data: {response.status_code}")
    return
  
  data = response.json()

  clear_deals()

  for item in data:
    name = item.get("name", "Unknown Item")
    price_str = item.get("price", 0)
    try: 
      price = float(price_str)
    except:
      price = 0.0
    insert_deal(name,price,STORE_NAME)

  print(f"Scraped {len(data)} items from {STORE_NAME}")

if __name__ == "__main__":
  scrape_flyer()