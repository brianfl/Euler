import math

def prime_check(n):
    for j in range(2, int(n**.5)+1):
        if n%j==0:
            return False
    return True

def distinct_pf(n):
    p_list = []
    n_t = n
    for i in range(2, int(n**.5)+1):
        if n_t%i==0:
            if prime_check(i):
                while True:
                    p_list.append(i)
                    n_t = int(n_t/i)
                    if n_t%i!=0:
                        break      
    prod = 1
    for h in p_list:
        prod*=h
    val = int(n/prod)
    if val!=1:
        p_list.append(val)
    return set(p_list)

def phi(n):
    l1 = distinct_pf(n)
    prod = 1
    for h in l1:
        prod *= (1-1/h)
    return round(prod*n)

sum1 = 0

for i in range(2, bound+1):
    sum1 += phi(i)

print(sum1) # 303963552391

"""
The number of total reduced proper fractions for any number
is the sum of all phi(n) from 2 to that number.
"""
 

        
            