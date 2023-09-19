#!/usr/bin/env python3

from app import app
from models import db, Dealership, Owner, Car
from faker import Faker
import random

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        print("Deleting old data...")

        Car.query.delete()
        Owner.query.delete()
        Dealership.query.delete()

        print("Seeding owners...")

        owners_list = []

        for _ in range(5):
            owner = Owner(
                first_name=faker.first_name(),
                last_name=faker.last_name()
            )
            owners_list.append(owner)

        db.session.add_all(owners_list)
        db.session.commit()

        print("Seeding dealerships...")

        dealerships_list = []

        for _ in range(5):
            dealer = Dealership(
                name=faker.company(),
                address=faker.street_address()
            )
            dealerships_list.append(dealer)

        db.session.add_all(dealerships_list)
        db.session.commit()

        print("Seeding cars...")

        cars_list = []
        manufacturers = ("Ford", "Chevrolet", "Toyota", "Chrysler", "Kia", "Tesla")

        for _ in range(10):
            car = Car(
                make=random.choice(manufacturers),
                model=faker.first_name(),
                date_sold=faker.date_between(start_date='-100y', end_date='today'),
                dealership=random.choice(dealerships_list),
                owner=random.choice(owners_list),
            )
            cars_list.append(car)

        db.session.add_all(cars_list)
        db.session.commit()

        print("Seeding complete!")