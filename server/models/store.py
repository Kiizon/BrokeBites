from db import db

class Store(db.Model):
    __tablename__ = 'stores'

    id                = db.Column(db.Integer, primary_key=True)
    name              = db.Column(db.String, unique=True, nullable=False)
    flipp_merchant_id = db.Column(db.String)

    # relationship: a store has many deals
    deals             = db.relationship('Deal', backref='store', lazy='dynamic')
