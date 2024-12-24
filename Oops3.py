class Student:
    def __init__(self):
        self.name = input("Enter the name: ")
        self.age = int(input("Enter the age: "))
        self.roll_number = int(input("Enter the roll_number: "))


    def show_data(self):
        print(f"The Name is: {self.name}")
        print(f"The Age is: {self.age}")
        print(f"The Roll number is: {self.roll_number}")


s1 = Student()
s2 = Student()

rn = int(input("Enter the roll number you want to find: "))

if s1.roll_number == rn:
    s1.show_data()

elif s2.roll_number == rn:
    s2.show_data()

else:
    print("No student with this roll number found")
    