import math

value = math.factorial(100)
s = str(value)

c = 0

for i in s:
    c += int(i)

print(c) # 648