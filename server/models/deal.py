from db import db
from datetime import datetime

class Deal(db.Model):
    __tablename__ = 'deals'
    id             = db.Column(db.Integer, primary_key=True)
    region_id      = db.Column(db.Integer, db.ForeignKey('regions.id'), nullable=False)
    store_id       = db.Column(db.Integer, db.ForeignKey('stores.id'),  nullable=False)
    flipp_flyer_id = db.Column(db.String)
    item           = db.Column(db.String, nullable=False)
    price          = db.Column(db.Numeric, nullable=False)
    scraped_at     = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
