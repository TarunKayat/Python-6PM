li = [43,67,35,47,234,57,847,6874,3234,5,243,65,73234]
num = int(input("Enter any Number: "))
flag = False
index = 0

# for i in range(0, len(li)):
#     if num == li[i]:
#         flag = True
#         print(f"The index is: {i}")
#         break

for i in li:
    if num == i:
        flag = True
        print(f"The index is: {index}")
        break

    index += 1 # 2

if not flag:
    print(f"{num} is not in the list")