def check_prime():
    num = int(input("Enter any Number: "))
    flag = False

    for i in range(2, num):
        if num % i == 0:
            flag = True
            break

    if flag == True:
        return True
    
    else:
        return False
    

x = check_prime()

if x == True:
    print("Composite")

else:
    print("Prime")