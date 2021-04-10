fac = 0

for i in range(1, int(600851475143**.5)+1):
    if 600851475143%i == 0:
        count = 0
        for j in range(2, int(i**.5)+1):
            if i%j == 0:
                count += 1
                break
        if count == 0 and i > fac:
            fac = i

print(fac) # 6857