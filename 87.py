primes = []

def is_prime(x):
    for i in range(2, int(x**.5)+1):
        if x%i==0:
            return False
    return True

for i in range(2, 7070): # 7070 is the largest possible value for a prime, from x**2 + 12 = 50M
    if is_prime(i):
        primes.append(i)

sums = set()
m = 50_000_000
for p in primes:
    if p**2>m:
        break
    else:
        for q in primes:
            if p**2+q**3>m:
                break
            else:
                for r in primes:
                    val = p**2+q**3+r**4
                    if val>m:
                        break
                    else:
                        sums.add(val)

print(len(sums)) # 1097343
