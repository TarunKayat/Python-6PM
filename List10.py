li = [34, 234, 65, 32, 67, 34, 24, 87, 4, 234, 23, 56]
n = len(li)

for i in range(0, n - 1):
    for j in range(0, n - i - 1):
        if li[j] > li[j + 1]:
            temp = li[j]
            li[j] = li[j + 1]
            li[j + 1] = temp


print("Sorted list")
print(li)