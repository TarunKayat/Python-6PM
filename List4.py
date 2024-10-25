li = [4,5657,354,683,4,54,565,7,8,4,6789,545,62,34,56754,6,7847,35,673,234,567,4, 3656]
num = int(input("Enter any Number: "))
count= 0
flag = False

for i in li:
    if num == i:
        flag = True
        count += 1 

if flag:
    print(f"{num} is in the list and was repeated {count} times")
else:
    print(f"{num} is not in the list")
    