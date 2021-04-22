import decimal as D
import math

D.getcontext().prec = 1000

sum1 = 0

for j in range(1, 101):
    if not ((j**(.5)).is_integer()):
        num = D.Decimal(j)
        sq2 = num.sqrt()
        for i in str(sq2)[2:101]:
            try:
                sum1 += int(i)
            except:
                pass
        sum1 += math.floor(sq2)

print(sum1) # 40886