class A:
    def fun1(self):
        print("First function of base class")

class B:
    def fun2(self):
        print("Second funtion of base class")

class C(A, B):
    def fun3(self):
        print("Function of child class")
        

obj = C()
obj.fun1()
obj.fun2()
obj.fun3()
