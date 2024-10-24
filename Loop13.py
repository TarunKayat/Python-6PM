num = int(input("Enter any Number: "))
rem = 0
result = 0
q = num

while num != 0: 
    rem = num % 10 
    result = result * 10 + rem
    num = num // 10

if result == q:
    print("Palindrome")

else:
    print("Not Palindrome")