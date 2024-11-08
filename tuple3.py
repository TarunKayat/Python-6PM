tup = (45, 234, 56, 324, 78, 54, 123, 45, 78, 54, 32)
num = int(input("Enter any Number: "))
li = list(tup)

if num in tup:
    li.remove(num)
    tup = tuple(li)
    print(f"{num} was in the tuple and now is removed new tuple")

else:
    li.append(num)
    tup = tuple(li)
    print(f"{num} was not in the tuple and now is added new tuple")

print(tup)
