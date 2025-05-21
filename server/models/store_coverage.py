from db import db

class StoreCoverage(db.Model):
    __tablename__ = 'store_coverage'
    store_id  = db.Column(db.Integer, db.ForeignKey('stores.id'),  primary_key=True)
    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'), primary_key=True)
