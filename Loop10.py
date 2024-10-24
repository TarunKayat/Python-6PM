num = int(input("Enter any Number: "))
count = 0

while num != 0: # 0
    num = num // 10
    count += 1 # 4

print(f"The number of Digits are: {count}")