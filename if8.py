gender = input("Enter Your gender: ")
age = int(input("Enter Your age: "))

if gender == 'female' and 18 <= age <= 25:
    print("You are eligible for Women's Scholarship")

elif gender == 'male':
    print("You are not eligible for Women's Scholarship")

else:
    print("You are not eligible for any Scholarship")