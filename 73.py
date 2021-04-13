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

def rel_prime(n):
    low = 1/3
    high = 1/2
    l1 = []
    s1 = distinct_pf(n)
    for i in range(int(low*n)+1, int(high*n)+1):
        if len(distinct_pf(i).intersection(s1))==0:
            l1.append(i)
    return l1

sum1 = -1
bound = 12000

for i in range(2, bound+1):
    sum1 += len(rel_prime(i))

print(sum1) # 7295372

 