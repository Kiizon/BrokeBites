from repos.region_repo import mark_region_scraped, get_region
from repos.store_repo  import upsert_store
from repos.deal_repo   import upsert_deal
from scraper import fetch_and_upsert_deals_for_fsa
from datetime import datetime, timezone, timedelta


FRESHNESS_THRESHOLD = timedelta(days=7)
def store_flyers_and_deals(postal_code: str):
    fsa    = postal_code[:3].upper()

    region = get_region(fsa)

    # if region doesnt exist or has not been scraped in a while
    if (region is None or 
        region.last_scrape is None or 
        datetime.now(timezone.utc).replace(tzinfo=None) - region.last_scrape.replace(tzinfo=None) > FRESHNESS_THRESHOLD):

        region = mark_region_scraped(fsa)
        fetch_and_upsert_deals_for_fsa(postal_code, region.id)

