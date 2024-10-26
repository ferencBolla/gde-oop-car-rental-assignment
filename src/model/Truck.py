from .Car import Car


class Truck(Car):
    def __init__(self, license_plate, car_type, rental_fee, load_capacity_in_kg):
        super().__init__(license_plate, car_type, rental_fee)
        self.load_capacity = load_capacity_in_kg

    def info(self):
        return (f"Truck: {self.license_plate}, Type: {self.car_type}, "
                f"Load Capacity: {self.load_capacity} kg, Rental Fee: {self.rental_fee} EUR/day")
