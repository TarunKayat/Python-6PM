s = input("Enter the string: ")
find_chr = input("Enter the character you want to find: ")

if find_chr in s:
    print(f"{find_chr} is in the string")
else:
    print(f"{find_chr} is not in the string")