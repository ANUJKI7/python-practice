class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def display(self):
        super().display()
        print("Seats:", self.seats)


class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def display(self):
        super().display()
        print("Engine CC:", self.engine_cc)


car = Car("Toyota", "Fortuner", 7)
bike = Bike("Yamaha", "R15", 155)

print("Car Details:")
car.display()

print("\nBike Details:")
bike.display()