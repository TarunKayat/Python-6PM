for i in range(1, 501):
    flag = False

    for j in range(2, i):
        if i % j == 0:
            flag = True
            break

    if flag:
        print(f"{i} is composite")

    else:
        print(f"{i} is prime")