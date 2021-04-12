import math

rat = 3/7
d_bound = 1000000
n_bound = math.floor(rat*d_bound)

fractions = {}

for i in range(-100,100):
    for j in range(-100, 0):
        distance = rat - (n_bound+i)/(d_bound+j)
        fractions[distance] = str(n_bound+i)

min1 = 100
str1 = ''
for i in fractions:
    if i>0 and i<min1:
        min1 = i
        str1 = fractions[i]

print(str1) # 428570

"""

We know the answer will be a fraction around the 3/7 ratio,
so we just need to search around there.

"""