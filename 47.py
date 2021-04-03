list_primes = [2]

for i in range(3, 1000):
    counter = 0
    for j in list_primes:
        if j > int(i**.5) + 1:
            break
        if i % j == 0:
            counter += 1
            break
    if counter == 0:
        list_primes.append(i)

comps = {}

for i in range(210, 200000):
    p_count = 0
    for j in list_primes:
        if i % j == 0:
            p_count += 1
    if p_count == 4:
        comps[i] = True

for key in comps:
    try:
        if comps[key-1] and comps[key-2] and comps[key-3]:
            target = key-3
    except:
        pass

print(target) # 134043