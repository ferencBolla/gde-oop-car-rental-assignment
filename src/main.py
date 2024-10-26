import json
import random
from datetime import datetime, timedelta
from model import CarRentalCompany, PassengerCar, Truck

def main():
    config = {}
    with open('config.json', 'r') as file:
        config = json.load(file)

    rental_company = CarRentalCompany("Best Car Rental")

    initialize_rental_company(config, rental_company)
    load_initial_rentals(config, rental_company)

    while True:
        print("\n-- Car Rental System --")
        print("1. Rent a Car")
        print("2. Cancel Rental")
        print("3. List Current Rentals")
        print("4. List Rentable Cars")
        print("5. Exit")

        choice = input("Please select an option (1-5): ")
        if choice == "1":
            register_rental(rental_company)
        elif choice == "2":
            cancel_rental_reservation(rental_company)
        elif choice == "3":
            list_rentals(rental_company)
        elif choice == "4":
            list_cars(rental_company)
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

def initialize_rental_company(config, rental_company):
    cars = config["cars"]
    for car in cars:
        if car["type"] == "PassengerCar":
            rental_company.add_car(
                PassengerCar(car["license_plate"], car["model"], car["price"], car["capacity"]))
        elif car["type"] == "Truck":
            rental_company.add_car(
                Truck(car["license_plate"], car["model"], car["price"], car["capacity"]))

def load_initial_rentals(config, rental_company):
    initial_rental_numbers = config["initial_rental_numbers"]
    customers = config["initial_customers"]
    cars = config["cars"]

    num_rentals = min(initial_rental_numbers, len(cars))
    for _ in range(num_rentals):
        customer = random.choice(customers)
        car = random.choice(cars)
        rental_date = random_rental_date()

        rental_company.rent_car(customer, car["license_plate"], rental_date)

def random_rental_date():
    return (datetime.now() + timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d')

def register_rental(rental_company):
    customer_name = input("Enter your name: ")
    license_plate = input("Enter the car's license plate: ")
    rental_date = input("Enter the rental date (YYYY-MM-DD): ")
    rental_company.rent_car(customer_name, license_plate, rental_date)

def cancel_rental_reservation(rental_company):
    customer_name = input("Enter your name: ")
    license_plate = input("Enter the car's license plate: ")
    rental_date = input("Enter the date of the rental to cancel (YYYY-MM-DD): ")
    rental_company.cancel_rental(customer_name, license_plate, rental_date)

def list_rentals(rental_company):
    print("\nCurrent Rentals:")
    rental_company.list_current_rentals()

def list_cars(rental_company):
    print("\nRentable Cars:")
    rental_company.list_all_cars()

if __name__ == "__main__":
    main()