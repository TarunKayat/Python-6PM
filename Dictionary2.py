dic1 = {"Name": "John", "age": 20, "email": "John@test.com"}
key = input("Enter the key: ")

if key in dic1:
    print(f"{key} is in the dictionary")

else:
    print(f"{key} is not in the dictionary")