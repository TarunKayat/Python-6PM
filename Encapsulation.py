class Student:
    def __init__(self, age, name, roll_number):
        self.__age = age
        self.name = name
        self._roll_number = roll_number

    def show(self):
        print(f"The name is: {self.name}")
        print(f"The age is: {self.__age}")
        print(f"The roll number is: {self._roll_number}")


s1 = Student(12, "John", 1)
# s1.show()
# print(s1.age)
print(s1._roll_number)
print(s1.__age)
