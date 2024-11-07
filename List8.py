li = [45, 34, 56, 67, 35, 24, 56, 87, 34, 234, 46, 23, 56, 34, 23]
Min = li[0]
Max = li[0]

for i in range(1, len(li)):
    if li[i] < Min:
        Min = li[i] 

    if li[i] > Max:
        Max = li[i] 

secmin = Max
secmax = Min

for i in li:
    if i != Min:
        if i < secmin:
            secmin = i 

    if i != Max:
        if i > secmax:
            secmax = i

print(f"The Minimum number is list is: {Min}")
print(f"The second smallest number is list is: {secmin}")
print(f"The Maximum number is list is: {Max}")
print(f"The second largest number is list is: {secmax}")