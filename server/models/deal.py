from app import db
from datetime import datetime

class Deal(db.Model):
    __tablename__ = "deals"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    original_price = db.Column(db.Float)
    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Deal {self.title}>'

    def to_dict(self):
        return {
            'store': self.store_name,
            'item':  self.item_name,
            'price': float(self.price),
            'scraped_at': self.scraped_at.isoformat(),
        }