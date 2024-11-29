class Vehical:
    def __init__(self):
        print("This is a vehical")


class Car(Vehical):
    def __init__(self):
        super().__init__()
        print("This is a car")


class Racing:
    def __init__(self):
        print("This is for racing")


class Ferreri(Car, Racing):
    def __init__(self):
        super().__init__()
        print("Ferreri is a racing car")


obj = Ferreri()
        