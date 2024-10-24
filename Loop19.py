for i in range(1, 501):
    rem = 0
    result = 0
    q = i

    while q != 0:
        rem = q % 10
        result = result * 10 + rem
        q = q // 10


    if result == i:
        print(f"{i} is Palindrome")

    # else:
    #     print(f"{i} is not Palindrome")