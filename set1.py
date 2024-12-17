s1 = {1, 2, 3, 4}
s2 = {1, 2, 3}

is_subset = True
for elem in s2:
    if elem not in s1:
        is_subset = False
        break

if is_subset:
    print("s2 is a subset of s1")
else:
    print("s2 is not a subset of s1")
