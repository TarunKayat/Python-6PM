# Write a C program to determine eligibility for admission to a professional course based on the following criteria: Go to the editor
# Eligibility Criteria : Marks in Maths >=65 and Marks in Phy >=55 and Marks in Chem>=50 and Total in all three subject >=190 or Total in Maths and Physics >=140 ------------------------------------- Input the marks obtained in Physics :65 Input the marks obtained in Chemistry :51 Input the marks obtained in Mathematics :72 Total marks of Maths, Physics and Chemistry : 188 Total marks of Maths and Physics : 137 The candidate is not eligible.

Math = int(input("Enter the marks for Math: "))
Physics = int(input("Enter the marks for Physics: "))
Chemistry = int(input("Enter the marks for Chemistry: "))

total_marks = Physics + Math + Chemistry
math_Physics = Math + Physics

if (Math >= 65 and Physics >= 55 and Chemistry >= 50 and total_marks >= 190) or (math_Physics >= 140):
    print("Eligible")
else:
    print("Not Eligible")