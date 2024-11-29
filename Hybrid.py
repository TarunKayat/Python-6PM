class Vehical:
    def vehical(self):
        print("This is a vehical")


class Car(Vehical):
    def car(self):
        print("This is car")


class Racing:
    def racing(self):
        print("This is for racing")


class ferreri(Racing, Car):
    def fun(self):
        print("ferreri is a racing car")

    
obj = ferreri()
obj.vehical()
obj.car()
obj.racing()
obj.fun()