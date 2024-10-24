num = int(input("Enter any Number: "))

for i in range(1, num + 1):
    print(f"The cube of {i} is: {i ** 3}")


i = 1

while i <= num:
    print(f"The cube of {i} is: {i ** 3}")
    i += 1