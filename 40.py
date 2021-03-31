d = ''

for i in range(1, 1000000):
    d += str(i)

prod = int(d[1-1]) * int(d[10-1]) * int(d[100-1]) * int(d[1000-1]) * int(d[10000-1]) * int(d[100000-1]) * int(d[1000000-1])

print(prod) # 210