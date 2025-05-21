from db import db
from models.store import Store

def upsert_store(name: str, flipp_merchant_id: str = None):
    store = Store.query.filter_by(name=name).first()
    if not store:
        store = Store(name=name, flipp_merchant_id=flipp_merchant_id)
        db.session.add(store)
        db.session.commit()
    return store
