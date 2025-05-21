from datetime import datetime, timezone
from db import db
from models.region import Region

def get_region(fsa: str):
    return Region.query.filter_by(fsa=fsa).first()

def mark_region_scraped(fsa: str) -> Region:
    now    = datetime.now(timezone.utc).replace(tzinfo=None)  # Convert to naive UTC
    region = Region.query.filter_by(fsa=fsa).first()
    if not region:
        region = Region(fsa=fsa, last_scrape=now)
    else:
        region.last_scrape = now
    db.session.add(region)
    db.session.commit()
    return region
