Hardness = int(input("Enter the Hardness: "))
Carbon_Content = float(input("Enter the Carbon Content: "))
Tensile_strength = int(input("Enter the Tensile Strength: "))

hh = False
cc = False
ts = False

if Hardness > 50:
    hh = True

if Carbon_Content < 0.7:
    cc = True

if Tensile_strength > 5600:
    ts = True


if hh == True and cc == True and ts == True:
    print("Grade of Steel is 10")

elif hh == True and cc == True and ts == False:
    print("Grade of Steel is 9")

elif hh == False and cc == True and ts == True:
    print("Grade of Steel is 8")

elif hh == True and cc == False and ts == True:
    print("Grade of Steel is 7")

elif hh == True or cc == True or ts == True:
    print("Grade of Steel is 6")

else:
    print("Grade of Steel is 5")
