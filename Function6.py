def reverse():
    num = int(input("Enter any Number: "))
    q = num
    rem = 0
    result = 0

    while q != 0:
        rem = q % 10
        result = result * 10 + rem
        q = q // 10

    return num, result


def check_palindrome():
    num, result = reverse()

    if num == result:
        return True
    
    else:
        return False
    

# x = check_palindrome()

if check_palindrome():
    print("Palindrome")

else:
    print("Not Palindrome")
