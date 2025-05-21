from db import db

class Region(db.Model):
    __tablename__ = 'regions'

    id          = db.Column(db.Integer, primary_key=True)
    fsa         = db.Column(db.String, unique=True, nullable=False)
    last_scrape = db.Column(db.DateTime)

    # relationship: a region has many deals
    deals       = db.relationship('Deal', backref='region', lazy='dynamic')
  