class A:
    def __init__(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))


class B(A):
    def __init__(self):
        super().__init__()
        print(f"Prodcut = {self.a * self.b}")


class C(A):
    def __init__(self):
        super().__init__()
        print(f"Sum = {self.a + self.b}")


obj1 = B()
obj2 = C()