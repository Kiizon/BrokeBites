# repositories/deal_repo.py
from datetime import datetime, timezone
from db import db
from models.deal import Deal

def upsert_deal(region_id, store_id, flipp_flyer_id, item, price, scraped_at):
    deal = Deal.query.filter_by(
        region_id=region_id,
        store_id=store_id,
        item=item
    ).first()

    now = datetime.now(timezone.utc)
    if not deal:
        deal = Deal(
            region_id      = region_id,
            store_id       = store_id,
            flipp_flyer_id = flipp_flyer_id,
            item           = item,
            price          = price,
            scraped_at     = scraped_at
        )
    else:
        deal.price          = price
        deal.flipp_flyer_id = flipp_flyer_id
        deal.scraped_at     = now

    db.session.add(deal)
    db.session.commit()
    return deal
