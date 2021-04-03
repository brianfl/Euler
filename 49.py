list_primes = [2]

for i in range(3, 10000):
    counter = 0
    for j in list_primes:
        if j > int(i**.5) + 1:
            break
        if i % j == 0:
            counter += 1
            break
    if counter == 0:
        list_primes.append(i)

list_4_dig_primes = [i for i in list_primes if len(str(i)) == 4]

perm_dict = {i:[] for i in list_4_dig_primes}

for i in list_4_dig_primes:
    temp_list = []
    s_i = str(i)
    for j in list_4_dig_primes:
        s_j = str(j)
        counter = 0
        for k in range(0, 4):
            if s_i.count(s_i[k]) == s_j.count(s_i[k]):
                counter += 1
        if counter == 4:
            perm_dict[i].append(j)

perm_set = set()

for i in perm_dict:
    perm_set.add(tuple(perm_dict[i][::-1]))

full_d_list = []

target = ''

for tup in perm_set:
    for ind, val in enumerate(tup):
        for ind2, val2 in enumerate(tup[ind+1:]):
            pri_diff = val - val2
            for val3 in tup[ind2+1:]:
                if val2 - val3 == pri_diff and tup[0] != 8741:
                    target += str(val3) + str(val2) + str(val)

print(target) # 296962999629