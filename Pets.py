class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hungry = True

    def eat(self):
        self.hungry = False

class Pets(Animal):
    pet_list = []
    pet_hungry = []
    def __init__(self,name,age):
       self.pet_list.append(Animal.__init__(self, name, age))

    def is_hungry(self):
        for i in range():
            if self.pet_list[i][2] == True:
                print (True)
                self.pet_hungry.append(self.pet_list[i])

    def whos_hungry(self):
        for i in range(len(self.pet_hungry)):
            print(self.pet_hungry[i])

class Cat(Animal):
    species = "Felis Catus"
    def sound(self):
        print("Meow")

class Dog(Animal):
    species = "Canis Lupus"
    def sound(self):
        print("Woof")

class Bird(Animal):
    species = "Palaeognathae"
    def sound(self):
        print("Chirp")


Peliharaan = Pets("Tibu",12)
Peliharaan.is_hungry()