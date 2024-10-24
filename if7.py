temp = int(input("Enter the temperature: "))

if temp < 0:
    print("Freezing weather ")

elif 0 <= temp < 10:
    print("Very Cold weather ")

elif 10 <= temp < 20:
    print("Cold weather")

elif 20 <= temp < 30:
    print("Normal Weather")

elif 30 <= temp < 40:
    print("Hot Weather")

else:
    print("Very Hot Weather")