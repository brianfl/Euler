def is_prime(current_primes, potential):
    counter = 0
    for i in current_primes:
        if potential % i == 0:
            counter += 1
    if counter == 0:
        return True
    else:
        return False

prime_list = [2]

for i in range(3, 1001):
    if is_prime(prime_list, i):
        prime_list.append(i)

prime_list.remove(2)
prime_list.remove(5)

longest_order = 0
curr_highest = 0
for i in prime_list:
    order = False
    power = 1
    while not order:
        curr_order = 10**power % i
        if curr_order == 1:
            if power > longest_order:
                longest_order = power
                curr_highest = i
            order = True
        else:
            power += 1

print(curr_highest) # 983

"""

Learned a lot of new math today on repeating decimals, cyclic numbers, and modular arithmetic...
A lot of trouble brute forcing this. Switched to research & formulas which worked.

"""