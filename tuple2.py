tup = (34, 32, 7, 34, 132, 87, 34, 12, 789, 23)
Min = tup[0]
Max = tup[0]

for i in range(1, len(tup)):
    if tup[i] < Min:
        Min = tup[i] 

    if tup[i] > Max:
        Max = tup[i] 

print(f'The Minimum number in tuple is: {Min}')
print(f'The Maximum number in tuple is: {Max}')