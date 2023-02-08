from config import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    weight = db.Column(db.float, nullable=False)
    description = db.Column(db.String(160), nullable=False)