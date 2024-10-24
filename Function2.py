def check_prime():
    num = int(input("Enter any Number: "))
    flag = False

    for i in range(2, num):
        if num % i == 0:
            flag = True
            break

    if flag:
        print("Composite")

    else:
        print("Prime")

check_prime();