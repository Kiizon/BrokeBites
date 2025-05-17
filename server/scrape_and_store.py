import requests, random
from datetime import datetime
from database import get_connection
from db_ops import (
    upsert_postal_code, upsert_flyer,
    link_flyer_to_postal, insert_sale_items
)

DATA_URL  = "https://flyers-ng.flippback.com/api/flipp/data?locale=en&postal_code={}&sid={}"
ITEMS_URL = "https://flyers-ng.flippback.com/api/flipp/flyers/{}/flyer_items?locale=en&sid={}"
GROCERY   = {"No Frills"}

def gen_sid():
    return "".join(str(random.randint(0,9)) for _ in range(16))

def fetch_flyers(postal_code):
    sid = gen_sid()
    url = DATA_URL.format(postal_code, sid)
    r = requests.get(url); r.raise_for_status()
    data = r.json().get("flyers") or r.json().get("data", {}).get("flyers", [])
    return [f for f in data if f.get("merchant") in GROCERY]

def fetch_items(flyer_id):
    sid = gen_sid()
    url = ITEMS_URL.format(flyer_id, sid)
    r = requests.get(url); r.raise_for_status()
    payload = r.json()
    return payload.get("flyer_items") or payload.get("data", {}).get("items", []) or []

def main(postal_code):
    db = SessionLocal()
    try:
        upsert_postal_code(db, postal_code)

        flyers = fetch_flyers(postal_code)
        for f in flyers:
            fid  = f["id"]
            store = f["merchant"]
            date  = datetime.utcnow().date()
            
            upsert_flyer(db, fid, store, date)
            link_flyer_to_postal(db, postal_code, fid)

            items = fetch_items(fid)
            insert_sale_items(db, fid, items)

            print(f"Stored {len(items)} items from flyer {fid}")
    finally:
        db.close()

if __name__ == "__main__":
    main("M5V3L9")
