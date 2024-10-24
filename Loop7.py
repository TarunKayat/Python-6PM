num = int(input("Enter any Number: "))
evensum = 0
oddsum = 0
i = 1

while i <= num: 
    if i % 2 == 0:
        evensum = evensum + i 

    else:
        oddsum = oddsum + i 

    i += 1 

print(f"The sum of all even numbers is: {evensum}")
print(f"The sum of all odd numbers is: {oddsum}")
