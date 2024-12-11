str = input("Enter the string: ")
ucount = 0
lcount = 0
dcount = 0
scount = 0

for i in str:
    if  i.isupper():
        ucount += 1

    elif i.islower():
        lcount += 1

    elif i.isdigit():
        dcount += 1

    else:
        scount += 1


print(f"The number of uppercase letters are: {ucount}")
print(f"The number of lowercase letters are: {lcount}")
print(f"The number of special characters are: {scount}")
print(f"The number of digits are: {dcount}")