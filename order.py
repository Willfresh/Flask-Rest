from config import db
from datetime import datetime

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)