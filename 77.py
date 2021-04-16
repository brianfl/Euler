import math

def prime_check(n):
    for j in range(2, int(n**.5)+1):
        if n%j==0:
            return False
    return True

def distinct_pf_sum(n):
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
    sum1 = 0
    for j in set(p_list):
        sum1 += j
    return sum1

d1 = {0:1, 1:0}

def a_n(n):
    sum1 = 0
    for i in range(1, n+1):
        sum1 += ((distinct_pf_sum(i) * d1[n-i]))
    d1[n] = (sum1*(1/n))
    return sum1*(1/n)

incr = 2
stop = False
while not stop:
    val1 = a_n(incr)
    if val1 > 5_000:
        target = incr
        stop = True
    else:
        incr += 1        

print(target) # 71

"""

Using a formula from OEIS.

Still not entirely sure how this formula and the one from 76 work...

"""
 
