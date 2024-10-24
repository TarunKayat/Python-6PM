pcount = 0
ncount = 0
zcount = 0

while True:
    num = int(input("Enter any Number: "))

    if num > 0:
        pcount += 1

    elif num == 0:
        zcount += 1

    else:
        ncount += 1

    choice = input("Do you want to continue: ")

    if choice == 'no':
        break


print(f"The number of Positive values are: {pcount}")
print(f"The number of Negative values are: {ncount}")
print(f"The number of Zeros are: {zcount}")
