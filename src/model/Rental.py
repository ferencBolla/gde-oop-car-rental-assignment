from datetime import datetime, date


class Rental:
    def __init__(self, car, rental_date, customer_name):
        self.car = car

        if isinstance(rental_date, str):
            self.rental_date = datetime.strptime(
                rental_date, "%Y-%m-%d").date()
        elif isinstance(rental_date, date):
            self.rental_date = rental_date
        else:
            raise ValueError("Invalid date format.")
        
        self.customer_name = customer_name

    def info(self):
        return (f"{self.customer_name} rented the car with license plate {self.car.license_plate} "
                f"on {self.rental_date}, Rental Fee: {self.car.rental_fee} EUR")
