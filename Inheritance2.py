class Base:
    def __init__(self):
        print("Hello form parent class")


class Derived(Base):
    def __init__(self):
        print("Hello from child class")
        super().__init__()

#    def fun(self):
#        print("hello")


obj = Derived()
# obj.fun()
# obj.greet()