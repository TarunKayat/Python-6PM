num = int(input("Enter any Number: "))
rem = 0
result = 0

while num != 0:
    rem = num % 10 
    result = result + rem 
    num = num // 10

print(f"The sum of all digits is: {result}")