# ================================ Vehicle Fleet System ================================

# Build: Vehicle (base) Car, Truck, Motorcycle (single inheritance). Car ElectricCar (multilevel). Use super() correctly at every level. Add fuel_cost(km) method overridden in each class with different rates. Track total vehicles via a class variable.

#(Hint: ElectricCar should override fuel_cost() returning 0; use isinstance() in a fleet report /function)



# ================================ Vehicle Fleet System ================================

class Vehicle:
    _count = 0

    def __init__(self, brand):
        self.brand = brand
        Vehicle._count += 1

    def fuel_cost(self, km):
        return 0

    def describe(self):
        return f"Brand = {self.brand}"

    @classmethod
    def total_vehicles(cls):
        return cls._count


class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def fuel_cost(self, km):
        return km * 8


class Truck(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def fuel_cost(self, km):
        return km * 15


class Motorcycle(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def fuel_cost(self, km):
        return km * 4


class ElectricCar(Car):
    def __init__(self, brand):
        super().__init__(brand)

    def fuel_cost(self, km):
        return 0


def fleet_report(vehicles, km):
    for vehicle in vehicles:
        print(vehicle.describe())
        print("Fuel Cost =", vehicle.fuel_cost(km))

        if isinstance(vehicle, ElectricCar):
            print("Type : Electric Car")

        print()


fleet = [Car("Honda"),Truck("Tata"),Motorcycle("Yamaha"),ElectricCar("Tesla")]

fleet_report(fleet, 100)

print("Total Vehicles =", Vehicle.total_vehicles())































































