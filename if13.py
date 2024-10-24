# Century Year - 2000 1200 1500 1600 1800 % 100 % 400
# Non-Century Year - 2024 2023 1991 1972 % 4

year = int(input("Enter any Number: "))

if year % 100 == 0: 
    if year % 400 == 0:
        print("Leap year and Century year")

    else:
        print("Century year not a leap year")

else:
    if year % 4 == 0:
        print("Leap year non-century year")

    else:
        print("Non-century year not a leap year")