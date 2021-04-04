list_primes = {2:True}

for i in range(3, 1000000*3):
    counter = 0
    for j in list_primes:
        if i%j == 0:
            counter += 1
            break
        if j > (i**.5 + 1):
            break
    if counter == 0:
        list_primes[i] = True

target = 0

for prime in list_primes:
    s = str(prime)[::-1]
    if s.count("1") > 0: # Tried with zero, answer was wrong, stepped up to 1, answer was right.
        step = 0
        for index, value in enumerate(s):
            if value == '1':
                step += 10**index
        counter = 0
        for i in range(0, 10):
            try:
                if list_primes[prime + i*step]:
                    counter += 1
            except:
                pass
        if counter == 8:
            target = prime

print(target) # 121313

