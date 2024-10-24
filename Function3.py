def fun(choice):
    if choice == 1:
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

        print("==============================")

    elif choice == 2:
        num = int(input("Enter any Number: "))
        q = num 
        rem = 0
        result = 0

        while q != 0:
            rem = q % 10
            result = result * 10 + rem
            q = q // 10

        if result == num:
            print("Palindrome")
        else:
            print("Not Palindrome")

        print("==============================")

    elif choice == 3:
        num = int(input("Enter any number: "))
        count = 0
        q = num
        rem = 0
        mul = 1
        result = 0

        while q != 0:
            q = q // 10
            count += 1 

        q = num

        while q != 0: 
            rem = q % 10
            mul = rem ** count 
            result = result + mul 
            mul = 1
            q = q // 10

        if result == num:
            print("Armstrong")

        else:
            print("Not Armstrong")
        
        print("==========================")

    elif choice == 4:
        num = int(input("Enter any Number: "))
        a = -1
        b = 1
        c = 0

        for i in range(1, num + 1):
            c = a + b
            print(c)
            a = b
            b = c
        
        print("===============================")




print("Choose From Below Options");
print("1 For Prime Number")
print("2 For Palindrome Number")
print("3 For Armstrong Number")
print("4 For Fibonacci Series")
print("5 For Exit")
print("===============================")


while True:
    choice = int(input("Enter Your Choice: "));
    print("===============================")

    if choice == 1:
        fun(choice)

    elif choice == 2:
        fun(choice)


    elif choice == 3:
        fun(choice)

            
    elif choice == 4:
        fun(choice)

    elif choice == 5:
        print("Code Exited")
        break

    else:
        print("Invalid Choice")
        print("Try Again")
        print("==========================")

