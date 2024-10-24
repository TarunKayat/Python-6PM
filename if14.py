a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b:
    if a > c:
        print(f"{a} is greatest")

    else:
        print(f"{c} is greatest")

else:
    if b > c:
        print(f"{b} is greatest")

    else:
        print(f"{c} is greatest")