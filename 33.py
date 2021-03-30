set1 = set()
for i in range(11, 100):
    for j in range(11, 100):
        if i/j < 1:
            s_i = str(i)
            s_j = str(j)
            prod = i/j
            for k in s_i:
                for m in s_j:
                    if int(m) != 0 and not(s_i[0] == s_i[1]):
                        if int(k)/int(m) == prod and s_i.replace(k, '') == s_j.replace(m, ''):
                            if not (s_i.replace(k, '') == '0' or s_j.replace(m, '') == '0'):
                                set1.add((i, j))
num = 1
denom = 1

for i in set1:
    num = num * i[0]
    denom = denom * i[1]

print(denom/num) # 100