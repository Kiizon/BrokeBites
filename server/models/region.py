from app import db
from datetime import datetime

class Region(db.Model):
  __tablename__ = "regions"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False, unique=True)
  fsa         = db.Column(db.String(3), nullable=False, unique=True)
  last_scrape = db.Column(db.DateTime, default=None)
  deals = db.relationship('Deal', backref='region', lazy=True)

  def __repr__(self):
      return f"<Region {self.name}>"