class Vehile:
    def __init__(self, brand, model, year, km):
        self.brand = brand
        self.brand = brand
        self.year = year 
        self.km = km


class Car(Vehile):
    def __init__(self, brand, model, year, km, body_type):
        super().__init__(brand, model, year, km)
        self.body_type = body_type


class Truck(Vehile):
    def __init__(self, brand, model, year, km, lifityng_capacity):
        super().__init__(brand, model, year, km)
        self.lifityng_capacity = lifityng_capacity


class Motocyrcle(Vehile):
    def __init__(self, brand, model, year, km, engine_capacity):
        super().__init__(brand, model, year, km)
        self.engine_capacity = engine_capacity


class Fleet:
    def __init__(self):
        self.cars = []

    def add_vehicle(self, vehicle):
        self.cars.append(vehicle)    

    def search_vehicle(self, target):
            for i in self.cars:
                for j in i.__dict__.values():
                    if j == target:
                        return i


car = Car("BMW", "M5", 2020, 132, "")
truck = Truck("Tesla", "Cybertruck", 2021, 900, 200)
mtc = Motocyrcle("Honda", "RX23", 2019, 12200, 20)

fleet = Fleet()     
fleet.add_vehicle(car)
fleet.add_vehicle(truck)
fleet.add_vehicle(mtc)
fleet.search_vehicle(2020)    

print(fleet.search_vehicle(2021))