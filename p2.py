num = int(input("Enter any 4 Digit Number: "))
lastdigit = 0

lastdigit = num % 10
num = num // 1000
# num = num // 10 # 123
# num = num // 10 # 12
# num = num // 10 # 1

print(f"The sum of first and last digit is: {lastdigit + num}")