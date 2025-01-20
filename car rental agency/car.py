class Car:
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Name: {self.maker}")
        print(f"Car Name: {self.model}")
        print(f"Car Name: {self.year}")


num_cars = int(input("how many cars do you want to enter "))
cars = []
for _ in range(num_cars):
    maker = input("enter the cars name: ")
    model = input("enter the model: ")
    year = input("enter the year: ")
    car = Car(maker, model, year)
    cars.append(car)

for car in cars:
    car.display_info()
    print()