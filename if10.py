Physics = int(input("Enter the marks for Physics: "))
Chemistry = int(input("Enter the marks for Chemistry: "))
Biology = int(input("Enter the marks for Biology: "))
Math = int(input("Enter the marks for Math: "))
Computer = int(input("Enter the marks for Computer: "))

per = (Physics + Chemistry + Biology + Math + Computer) // 5

if 90 <= per <= 100:
    print("Grade A")

elif 80 <= per < 90:
    print("Grade B")

elif 70 <= per < 80:
    print("Grade C")

elif 60 <= per < 70:
    print("Grade D")

elif 40 <= per < 60:
    print("Grade E")

else:
    print("Grade F")


print(f"Your percentage is: {per}")