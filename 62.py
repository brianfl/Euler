target = 0

list_cubes = [i**3 for i in range(3, 10000)]
for i in list_cubes:
    perm_count = 0
    s_i = str(i)
    for j in list_cubes:
        s_j = str(j)
        if i!= j and len(s_j) == len(s_i):
            count = 0
            for char in s_i:
                if s_i.count(char) == s_j.count(char):
                    count += 1
            if count == len(s_i):
                perm_count += 1
    if perm_count == 4:
        target = i
        break

print(target) # 127035954683

"""
Sneaks under a minute.
"""