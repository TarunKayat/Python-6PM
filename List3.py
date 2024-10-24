li = [34, 345,56,47,245,7683,547,683,456,32,456,763,54678,34,567,34,67,35467,83,234,24,2,43,567,8,5,6789,483,213,456,34,23,56]
num = int(input("Enter any Number: "))

# if num in li:
#     print(f"{num} is in the list")

# else:
#     print(f"{num} is not in the list")

flag = False
for i in li:
    if i == num:
        flag = True
        print(f"{num} is in the list")
        break

if not flag:
    print(f"{num} is not in the list")