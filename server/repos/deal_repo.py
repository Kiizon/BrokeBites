from db import db
from datetime import timezone, datetime
from models.deal import Deal

def upsert_deal(region_id, store_id, flipp_flyer_id, item, price, scraped_at):
    try:
        price_value = float(price) if price and price.strip() else None
    except (ValueError, TypeError):
        print(f"Skipping deal for item '{item}' due to invalid price: '{price}'")
        return None

    deal = Deal.query.filter_by(
        region_id=region_id,
        store_id=store_id,
        item=item
    ).first()

    now = datetime.now(timezone.utc)
    if not deal:
        deal = Deal(
            region_id=region_id,
            store_id=store_id,
            flipp_flyer_id=flipp_flyer_id,
            item=item,
            price=price_value,
            scraped_at=scraped_at
        )
    else:
        deal.price = price_value
        deal.flipp_flyer_id = flipp_flyer_id
        deal.scraped_at = now

    try:
        db.session.add(deal)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error saving deal for item '{item}': {e}")
        return None

    return deal