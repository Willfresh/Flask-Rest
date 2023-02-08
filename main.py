from app import app
from config import db
from flask import jsonify, request


with app.app_context():
    db.create_all()
    


if (__name__ == '__main__'):
    app.run(debug=True)