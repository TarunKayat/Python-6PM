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