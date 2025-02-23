class Animal:
    def __init__(self, name, species, age, diet):
        self.name= name
        self.__species = species
        self.__age = age
        self.diet = diet

    def make_sound(self):
        print(f"Животное: {self.name} издает звук: ")    

class Mammal(Animal):
    def __init__(self, name, species, age, diet, fur_color):
        Animal.__init__(self, name, species, age, diet)        
        self.fur_color = fur_color

    def make_sound(self):
        Animal.make_sound(self)
        print("Муу")    


class Bird(Animal):
    def __init__(self, name, species, age, diet, winng_span):
        Animal.__init__(self, name, species, age, diet)        
        self.winng_span = winng_span

    def make_sound(self):
        Animal.make_sound(self)
        print("Кар")            


class ZoooEmployee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def feed_animal(self, animal):
        print("Работник, кормит животное: " + animal.name)  


class Visitor:
    def __init__(self, name, ticket_number):
        self.name = name
        self.ticket_number = ticket_number

    def watch_animal(self, animal):
        print(f"Посититель {self.ticket_number} смотрит {animal.name} ")   


cow = Mammal("Корова", "белая", 19, "трава", "пятнистая")
cow.make_sound()

crow = Bird("Ворона", "белая", 25, "орехи", "Отсутствует")
crow.make_sound()

empl = ZoooEmployee("Роберт", "Северная часть")
empl.feed_animal(crow)

visitor = Visitor("Кристофер", 1232)
visitor.watch_animal(cow)