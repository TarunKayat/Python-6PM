class fun:
    def setdata(self, a):
        self.a = a

    
    def show_data(self):
        print(f"The value is: {self.a}")

    def __add__(self, obj):
        result = fun()

        result.a = self.a + obj.a
        return result



obj1 = fun()
obj2 = fun()
obj3 = fun()
result = fun()

obj1.setdata(10)
obj2.setdata(50)
obj3.setdata(20)

result = obj1 + obj2 + obj3
result.show_data()