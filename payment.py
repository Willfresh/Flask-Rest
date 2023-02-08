from config import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    amount = db.Column(db.float, nullable=False)