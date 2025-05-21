from models.region import Region
from models.store  import Store
from models.deal   import Deal
from sqlalchemy    import distinct

def get_store_deals_for_region(fsa: str) -> dict[str, list[dict]]:
    """
    Returns a mapping { store_name: [ {item, price, unit}, … ], … }
    for all deals in the given FSA.
    """
    region = Region.query.filter_by(fsa=fsa).first()
    if not region:
        return {}

    stores = (
        Store.query
             .join(Deal, Deal.store_id == Store.id)
             .filter(Deal.region_id == region.id)
             .distinct()
             .all()
    )

    output = {}
    for store in stores:
        deals = (
            Deal.query
                .filter_by(region_id=region.id, store_id=store.id)
                .all()
        )
        output[store.name] = [
            {"item": d.item}
            for d in deals
        ]
    return output
