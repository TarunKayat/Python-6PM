from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(animal):
    def sound(self):
        print("Bark...")


class Cat(animal):
    def sound(self):
        print("Meow...")

d = Dog()
c = Cat()

d.sound()
c.sound()