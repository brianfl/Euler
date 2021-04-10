import decimal as Dec
import math

Dec.getcontext().prec = 100

def rome(n):

    n = Dec.Decimal(n).sqrt()

    a = []

    h_l = []
    k_l = []

    ite = 0

    while True:
        if ite == 0:
            a_n = Dec.Decimal(math.floor(n))
            a.append(a_n)
            h_l.append(a_n)
            k_l.append(Dec.Decimal(1))
            number = Dec.Decimal(1)/(n-a_n)
            ite += 1
        
        elif ite == 1:
            a_n = Dec.Decimal(math.floor(number))
            h = (a[0]*a_n + Dec.Decimal(1))
            k = a_n
            a.append(a_n)
            h_l.append(h)
            k_l.append(k)
            number = Dec.Decimal(1)/(number-a_n)
            ite += 1
        
        else:
            a_n = Dec.Decimal(math.floor(number))
            h = a_n * h_l[ite-1] + h_l[ite-2]
            k = a_n * k_l[ite-1] + k_l[ite-2]
            k_l.append(k)
            a.append(a_n)
            h_l.append(h)
            number = Dec.Decimal(1)/(number-a_n)
            ite += 1

        if abs(h_l[-1]**Dec.Decimal(2) - (n**Dec.Decimal(2))*(k_l[-1]**Dec.Decimal(2)) - Dec.Decimal(1)) < Dec.Decimal(.001) :
            return h_l[-1]

sqs = [i**2 for i in range(1, 101)]

ds = [i for i in range(1, 1001) if i not in sqs]

max_x = 0
max_d = 0

for i in ds:
    soln = rome(i)
    if soln > max_x:
        max_x = soln
        max_d = i

print(max_d) # 661

"""

Started with a brute force attempt based on when x and y had to be integers
based on when they were squares, one less than squares, that sort of thing...

Realized it would take too long, switched to research. Discovered this was
Pell's equtation, and you can solve it with a recurrence relationship based
on the continued fraction of Sqrt(D).

Definitely learned a thing or two...

"""