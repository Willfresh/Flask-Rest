from config import db
from datetime import datetime

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    date = db.Column(db.String, nullable=False)
    paymentId = db.Column(db.Integer, db.ForeignKey('payment.id'), nullable=True)