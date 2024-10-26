from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, license_plate, car_type, rental_fee):
        self.license_plate = license_plate
        self.car_type = car_type
        self.rental_fee = rental_fee
        self.booked_dates = []

    @abstractmethod
    def info(self):
        pass
