from random import randint

random_number = randint(1, 1000);

count = 0
while True:
    count += 1

    num = int(input("Guess the number: "))

    if num > random_number:
        print("Input number is greater try something smaller")

    elif num == random_number:
        print(f"7 Crore apne sahi number guess karliye {random_number} pata karne me try lage {count}")
        break

    else:
        print("Input number is samller try something greater")
