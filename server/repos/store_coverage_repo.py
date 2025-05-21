from db import db
from models.store_coverage import StoreCoverage

def upsert_store_coverage(store_id: int, region_id: int):
    """
    Ensure a StoreCoverage row exists for this store↔region pair.
    """
    cov = StoreCoverage.query.filter_by(
        store_id=store_id,
        region_id=region_id
    ).first()

    if not cov:
        cov = StoreCoverage(
            store_id=store_id,
            region_id=region_id
        )
        db.session.add(cov)
        db.session.commit()

    return cov
