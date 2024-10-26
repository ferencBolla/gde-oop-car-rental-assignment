from datetime import datetime, date
from .Rental import Rental


class CarRentalCompany:
    def __init__(self, name):
        self.name = name
        self.cars = []
        self.rentals = []

    def add_car(self, car):
        self.cars.append(car)

    def __add_rental(self, rental):
        self.rentals.append(rental)
        rental.car.booked_dates.append(rental.rental_date)

    def rent_car(self, customer_name, license_plate, rental_date):
        if isinstance(rental_date, str):
            try:
                rental_date = datetime.strptime(rental_date, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                return
        elif not isinstance(rental_date, date):
            print("Invalid date.")
            return

        if rental_date < date.today():
            print("Cannot rent for a past date.")
            return

        for car in self.cars:
            if car.license_plate == license_plate:
                if rental_date not in car.booked_dates:
                    rental = Rental(car, rental_date, customer_name)
                    self.__add_rental(rental)
                    print(f"Rental successful! The rental fee is: {
                          car.rental_fee} EUR")
                    return
                else:
                    print("The car is already booked on the given date.")
                    return
        print("No car found with the given license plate.")

    def cancel_rental(self, customer_name, license_plate, rental_date):
        if isinstance(rental_date, str):
            try:
                rental_date = datetime.strptime(rental_date, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                return
        elif not isinstance(rental_date, date):
            print("Invalid date.")
            return

        for rental in self.rentals:
            if (rental.customer_name == customer_name and
                rental.car.license_plate == license_plate and
                    rental.rental_date == rental_date):
                rental.car.booked_dates.remove(rental_date)
                self.rentals.remove(rental)
                print("Rental successfully canceled.")
                return
        print("No matching rental found.")

    def list_current_rentals(self):
        if not self.rentals:
            print("There are no current rentals.")
        else:
            for rental in self.rentals:
                print(rental.info())

    def list_all_cars(self):
        if self.cars:
            print("All Cars:")
            for car in self.cars:
                print(car.info())
        else:
            print("No cars available.")
