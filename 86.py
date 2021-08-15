m = 1800
while True:
    m += 1
    summ = 0
    for a in range(1, m+1):
        for c in range(1, 2*a):
            val3 = ((a**2 + (c)**2))**.5
            if val3.is_integer() == True:
                if c%2==0:
                    if c>a+1:
                        summ += (c/2-(c-a-1))
                    else:
                        summ += (c/2)
                else:
                    if c>a+1:
                        summ += (int(c/2)-(c-a-1))
                    else:
                        summ += (int(c/2))
            else:
                pass
    if summ>1_000_000:
        break

print(m) # 1818

"""
The idea behind this is that each distance is an integer if it is a square which is the sum of two squares,
but instead of checking 3 values, just check 2 and partition one of them according to constraints.

I made an inefficient version of this, which was enough to plot a graph of the answers that showed
the final answer should be around, but above, 1800. Explaining the m = 1800. This is definitley not
the most efficient solution.

"""
