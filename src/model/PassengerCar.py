from .Car import Car


class PassengerCar(Car):
    def __init__(self, license_plate, car_type, rental_fee, number_of_passengers):
        super().__init__(license_plate, car_type, rental_fee)
        self.number_of_passengers = number_of_passengers

    def info(self):
        return (f"Passenger Car: {self.license_plate}, Type: {self.car_type}, "
                f"Number of Passengers: {self.number_of_passengers}, Rental Fee: {self.rental_fee} EUR/day")
