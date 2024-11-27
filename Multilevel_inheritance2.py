class Animal:
    def __init__(self):
        print("I am an animal")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("I am Dog")

class BabyDog(Dog):
    def __init__(self):
        super().__init__()
        print("I am a baby dog")


obj = BabyDog()