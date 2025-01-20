class Animal:
    def make_sound(self):
        print("hawhaw")

class Dog(Animal):
    def make_sound(self):
        print("woof woof")

animal = Animal()
dog = Dog()

animal.make_sound()
dog.make_sound()