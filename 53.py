import math
count = 0

for n in range(1, 101):
    for r in range(1, 101):
        try:
            value = math.factorial(n) / ( math.factorial(r) * math.factorial(n-r))
            if value > 1000000:
                count += 1
        except:
            pass

print(count) # 4075
