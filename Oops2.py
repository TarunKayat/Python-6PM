class Student:
    def setdata(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number

    def show_data(self):
        print(f"The name is: {self.name}")
        print(f"The age is: {self.age}")
        print(f"The roll number is: {self.roll_number}")


s1 = Student()
s2 = Student()
s1.setdata("John", 12, 1)
s2.setdata("Rahul", 10, 2)
s1.show_data()
s2.show_data()