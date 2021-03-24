target_number = 0
increment = 0

while target_number == 0:
    sum1 = 0
    increment += 1
    for j in range(1, increment):
        sum1 += j
    factors = 0
    for k in range(1, int(sum1**.5)+1):
        if sum1 % k == 0:
            factors += 1
    factors = factors * 2

    if factors > 500:
        target_number = sum1

print(target_number) # 76576500