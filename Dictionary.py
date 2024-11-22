# dic = {"Name": "John", "age": 20, "email": "John@test.com"}
# print(dic)
# print(type(dic))
# print(dic["age"])

# dic1 = {"Name": "John", "age": 20, "email": "John@test.com"}
# dic2 = {"Contact": 34567, "Profession": "Developer"}

# dic1.update(dic2)
# dic1.pop("age")
# dic1.popitem()
# dic1.clear()
# print(dic1.get("N"))
# print(dic1["N"])
# print(dic1.values())
# print(dic1.keys())
# print(dic1.items())

# for key in dic1.keys():
#     print(f"The value on {key} is: {dic1[key]}")

# for value in dic1.values():
#     print(value)

# for key, value in dic1.items():
#     print(f"The value on {key} is: {value}")

# li = (1, 2, 3)
# dic = dict.fromkeys(li, "None")
# print(dic)

# dic1.setdefault("N", "Rahul")
# print(dic1)

# dic = dic1.copy()
# print(dic)

# dic1 = {"Name": "John", "age": 20, "email": "John@test.com"}

# del dic1["age"]

# value = dic1.pop("N", "This key does not exist")
# print(value)

li = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(0, 3):
    for j in range(0, 3):
        print(li[i][j])