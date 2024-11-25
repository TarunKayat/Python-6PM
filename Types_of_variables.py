class Student:

    school = "THE PRIME STEP"

    def __init__(self, name, age, roll_number):
            self.name = name
            self.age = age
            self.roll_number = roll_number

    def show_data(self):
          print(f"Name = {self.name}")
          print(f"Age = {self.age}")
          print(f"Roll number = {self.roll_number}")

s1 = Student("John", 12, 1)
s2 = Student("Rahul", 10, 2)

s1.show_data()
s2.show_data()

Student.school = "PRIME STEP"

print(s1.school)
print(s2.school)