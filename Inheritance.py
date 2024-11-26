class Base: # Superclass or Base Class
    def greet(self):
        print("Hello")

class Derived(Base): # Subclass or Derived Class
    pass


obj = Derived()
obj.greet()