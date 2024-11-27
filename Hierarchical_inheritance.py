class A:
    def setdata(self):
        self.a = int(input("Enter the first number: "))
        self.b = int(input("Enter the second number: "))


class B(A):
    def product(self):
        print(f"Product = {self.a * self.b}")

        return self.a, self.b

class C(A):
    def sum(self):
        print(f"sum = {self.a + self.b}")


obj1 = B()
obj1.setdata()
obj1.product()

obj2 = C()
obj2.setdata()
obj2.product()

# while True:
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         obj1.setdata()
#         obj1.product()

#     elif choice == 2:
#         obj2.setdata()
#         obj2.sum()

#     elif choice == 3:
#         break