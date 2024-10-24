num = int(input("Enter any Number: "))

for i in range(1, num + 1): 
    if i % 2 == 0:
        print(f"{i} is even")

    else:
        print(f"{i} is odd")