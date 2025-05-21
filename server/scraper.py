import requests
import random
from datetime import datetime, timezone
from repos.store_repo import upsert_store
from models.store import Store  # for type hinting, if you like
from repos.deal_repo import upsert_deal

FLYERS_ENDPOINT      = 'https://flyers-ng.flippback.com/api/flipp/data?locale=en&postal_code={}&sid={}'
GROCERY_STORES       = {'No Frills', 'FreshCo'}
DEALS_ENDPOINT = 'https://flyers-ng.flippback.com/api/flipp/flyers/{}/flyer_items?locale=en&sid={}'

def generate_sid():
    return ''.join(str(random.randint(0, 9)) for _ in range(16))

def fetch_and_upsert_stores(postal_code: str):
    """
    Fetches grocery flyers for this postal code, upserts each merchant
    into the DB, and returns the list of ORM Store objects.
    """
    sid    = generate_sid()
    url    = FLYERS_ENDPOINT.format(postal_code, sid)
    data   = requests.get(url).json()
    flyers = data.get('flyers', [])
    flyer_ids = []

    for f in flyers:
        merchant    = f.get('merchant')
        merchant_id = f.get('merchant_id')
        categories  = f.get('categories', [])
        if isinstance(categories, str):
            categories = [c.strip() for c in categories.split(',')]

        if merchant in GROCERY_STORES and 'Groceries' in categories:
            store = upsert_store(
                name=merchant,
                flipp_merchant_id=merchant_id
            )
            flyer_ids.append({
                'store': store,
                'flipp_flyer_id': f['id']})
    return flyer_ids

def fetch_and_upsert_deals_for_fsa(postal_code: str, region_id: int):
    """
    1) upsert stores & get flyer IDs
    2) for each flyer, fetch deals & upsert them
    """
    entries = fetch_and_upsert_stores(postal_code)

    for entry in entries:
        store    = entry['store']
        flyer_id = entry['flipp_flyer_id']

        sid       = generate_sid()
        url       = DEALS_ENDPOINT.format(flyer_id, sid)
        raw_deals = requests.get(url).json()

        for d in raw_deals:
          upsert_deal(
              region_id      = region_id,
              store_id       = store.id,
              flipp_flyer_id = flyer_id,  
              item           = d['name'],
              price          = d['price'],
              scraped_at     = datetime.now(timezone.utc)
          )

            

