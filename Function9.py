# Required and Default Arguments
# def fun(a = 10, b = 5):
#     print(f"The Addition is: {a + b}")

# fun(20, 30)

# Keyword Arguments
# def fun(name, age):
#     print(f"Hello {name} your age is {age}")

# fun(age=20, name="John")

# Variable Length Argument
# def fun(*args):
#     # print(args)
#     add = 0
#     for i in args:
#         add = add + i

#     print(add)

# fun(10, 20, 30, 40)

# Keyword Arbitry Argument
# def fun(**kwargs):
#     # print(kwargs)

#     for key, value in kwargs.items():
#         print(f"The value on {key} is: {value}")

# fun(name="John", age=20, email="John@test.com")

# Positional only Arguments
# def fun(name, /, age):
#     print(f"Hello {name} your age is {age}")

# fun("John", 20)

# Keyword only Arguments
# def fun(*, name, age):
#     print(f"Hello {name} your age is {age}")

# fun(name="John", age=20)

# dic1 = {"Name": "John", "age": 20, "email": "John@test.com"}
# def fun(Name, age, email=0):
#     print(f"Name = {Name}")
#     print(f"Age = {age}")
#     print(f"Email = {email}")

# fun(dic1["Name"], dic1["age"], dic1['email'])
# fun(**dic1)
