def __init__(car_instance, make, model, year):
    car_instance.make = make
    car_instance.model = model
    car_instance.year = year

def show_details(car_instance):
    print(f"Make: {car_instance.make}, Model: {car_instance.model}, Year Made: {car_instance.year}")

