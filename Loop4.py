num = int(input("Enter any Number: "))
evensum = 0
oddsum = 0

for i in range(1, num + 1): # 6 i = 6
    if i % 2 == 0:
        evensum = evensum + i # 12

    else:
        oddsum = oddsum + i # 9


print(f"The sum of all even numbers is: {evensum}")
print(f"The sum of all odd numbers is: {oddsum}")