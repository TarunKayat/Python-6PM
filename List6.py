li = [34,67,24,72,346,24,576,3,5472,643,563,54,763,4,567,56]
num = int(input("Enter any Number: "))

if num in li:
    li.remove(num)
    print(f"{num} was in the list and now is removed")
    print(li)

else:
    li.append(num)
    print(f"{num} was not in the list and now is added")
    print(li)
