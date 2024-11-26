class Base:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def show_data(self):
        print(f"The name is: {self.name}")
        print(f"The roll number is: {self.roll_number}")


class Derived(Base):
    def __init__(self, name, roll_number, course, age):
        super().__init__(name, roll_number)
        self.course = course
        self.age = age

    def print_data(self):
        print(f"The course is: {self.course}")
        print(f"The age is: {self.age}")


obj = Derived("John", 1, "nhi pata", 12)
obj2 = Derived("Rahul", 2, "nhi pata", 10)
obj.show_data()
obj.print_data()
obj2.show_data()
obj2.print_data()
        