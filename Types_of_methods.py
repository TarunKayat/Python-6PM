class fun:
    school = "THE PRIME STEP"

    @classmethod
    def cl_method(cls, new_school):
        cls.school = new_school
        print(cls.school)

    @staticmethod
    def add(a, b):
        print(f"The addition is: {a + b}")


obj = fun()
obj.add(12, 10)
fun.add(50, 5)
fun.cl_method("PRIME STEP")