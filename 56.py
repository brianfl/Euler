max_sum = 0

for a in range(0,100):
    for b in range(0, 100):
        s_num = str(a**b)
        sum1 = 0
        for i in str(s_num):
            sum1 += int(i)
        if sum1 > max_sum:
            max_sum = sum1

print(max_sum) # 972