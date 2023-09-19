#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime

from models import db, Dealership, Owner, Car

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.get('/')
def index():
    return "Hello world"


# POST /cars
@app.post('/cars')
def create_car():
    data = request.json

    new_car = Car(
        make=data["make"],
        model=data["model"],
        owner_id=data["owner_id"],
        dealership_id=data["dealership_id"],
        date_sold=datetime.date(**data["date_sold"])
    )

    db.session.add(new_car)
    db.session.commit()

    return jsonify( new_car.to_dict() ), 201


if __name__ == '__main__':
    app.run(port=5555, debug=True)