phi_list = {}

def naples(num):
    b_count = 0
    rel_list = []
    for i in range(1, num+1):
        count = 0
        for j in range(2, i):
            if num%j==0 and i%j==0:
                count += 1
                break
        if count==0:
            b_count += 1
            rel_list.append(i)
    phi_list[num] = b_count
    for val in rel_list:
        if val!=1:
            phi_list[val*num] = phi_list[val] * phi_list[num]

    return b_count

inc = 0
while True:
    inc += 1
    naples(inc)
    if max(phi_list) > 1000000:
        break
max1 = 0
max2 = 0
for i in phi_list:
    if i/phi_list[i] > max1:
        max1 = i/phi_list[i]
        max2 = i

print(max2) # 510510

"""

Using the fact that the totient function is multiplicative here.

Our answer was not going to be a prime, since n/phi(n) is
small for primes. So once we get over 1,000,000 in our list,
we know the only values left to be filled in are prime.
We don't have to check those.

"""