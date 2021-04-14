import math

count = 0

for i in range(1, 1000000):
    r = {}
    while True:
        r[i] = True
        sum1 = 0
        for j in str(i):
            sum1 += math.factorial(int(j))
        i=sum1
        try:
            if r[i]:
                if len(r)==60:
                    count += 1
                break
        except:
            pass
    
print(count) # 402

"""

I could speed this up by adding a memory of each chain...

"""