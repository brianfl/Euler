import math
import decimal as d

d.getcontext().prec = 1000

def montenegro(num, target, ite):
    it = ite

    x = num - math.floor(num)

    if abs(x - target) < .00001:
        return it
    else:
        return montenegro(d.Decimal(1)/x, target, ite+1)


invalids = [i**2 for i in range(0, 100)]
count = 0
for i in range(2, 10000):
    if i not in invalids:
        n = d.Decimal(i)
        target = n.sqrt() - math.floor(n.sqrt())
        
        if montenegro(d.Decimal(1)/target, d.Decimal(target), 1) % 2 == 0:
            pass
        else:
            count += 1

print(count) # 1322
