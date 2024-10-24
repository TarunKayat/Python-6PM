print("Choose from Below Options")
print("1 For Addition")
print("2 For Subtraction")
print("3 For Multiplication")
print("4 For Division")
print("============================")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("=============================")

choice = int(input("Enter Your choice: "))
print("=========================")

if choice == 1:
    print(f"The Addition is: {a + b}")

elif choice == 2:
    print(f"The Subtraction is: {a - b}")

elif choice == 3:
    print(f"The Multiplication is: {a * b}")

elif choice == 4:
    print(f"The Division is: {a // b}")

else:
    print("Invalid choice")