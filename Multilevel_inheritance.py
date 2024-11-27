class Animal:
   def animal(self):
      print("I am an animal")

class Dog(Animal):
   def bark(self):
      print("Barking...")

class BabyDog(Dog):
   def weep(self):
      print("Weeping...")

obj = BabyDog()
obj.animal()
obj.bark()
obj.weep()