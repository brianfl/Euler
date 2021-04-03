rolling_sum = 0
for i in range(1, 1001):
    rolling_sum += i**i

print(str(rolling_sum)[-10:]) # 9110846700