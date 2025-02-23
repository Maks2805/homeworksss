

class Cars:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def get_info(self): return f"Автомобиль: {self.brand} {self.model} {self.year}, цвет: {self.color}"   

bmw = Cars("BMW", "X5", 2020, "red")
toyota = Cars("Toyota", "carmi", 2017, "yellow")
audi = Cars("Audi", "A6", 2010, "black")

print(bmw.get_info())
print(toyota.get_info())
print(audi.get_info())