import math

triples = []

for n in range(1, 1224, 2): # max possible value 1224 from assuming m=n and solving quadratic
    for m in range(n, 1224, 2):
        if math.gcd(m, n) == 1:
            a = m*n
            b = (m**2 - n**2)/2
            c = (m**2 + n**2)/2
            if not(a==0 or b==0 or c==0 or a==1 or b==1 or c==1):
                if a+b+c <= 1_500_000:
                    triples.append(sorted([a,b,c]))

lengths = {}

for i in triples:
    l = i[0] + i[1] + i[2]

    try:
        if len(lengths[l]) > 0:
            s = lengths[l].copy()
            s.add(i[0])
            lengths[l] = s
    except:
        lengths[l] = set([i[0]])

n_list = []

for i in triples:
    k = 1
    a, b, c = i[0], i[1], i[2]
    l1 = k*(a+b+c)
    while l1 <= 1_500_000:
        n_list.append([a*k, b*k, c*k])
        k += 1
        l1 = k*(a+b+c)

for i in n_list:
    l = i[0] + i[1] + i[2]
    try:
        if len(lengths[l]) > 0:
            s = lengths[l].copy()
            s.add(i[0])
            lengths[l] = s
    except:
        lengths[l] = set([i[0]])

count = 0
for i in lengths:
    if len(lengths[i]) == 1:
        count += 1

print(count) # 161667

"""

Using a variant of Euclid's formula to generate primitive triples,
then generating all non-primitives based on those.

Could be cleaned up.

"""