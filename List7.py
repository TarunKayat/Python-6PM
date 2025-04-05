li = [45, 34, 56, 67, 35, 24, 56, 87, 34, 234, 46, 23, 56, 34, 23]
Min = li[0]
Max = li[0]

for i in range(1, len(li)):
    if li[i] < Min:
        Min = li[i] 

    if li[i] > Max:
        Max = li[i] 

print(f"The Minimum number in list is: {Min}")
print(f"The Maximum number in list is: {Max}")
