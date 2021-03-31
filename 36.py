rolling_sum = 0

for i in range(1, 1000001):
    s = str(i), bin(i)[2:]
    counter = 0
    for j in s:
        if len(j) % 2 == 0: #even
            if j[0:int(len(j)/2)] == j[::-1][0:int(len(j)/2)]:
                counter += 1 
        else: # odd
            if j[0:int(len(j)/2)+1] == j[::-1][0:int(len(j)/2)+1]:
                counter += 1
    if counter == 2:
        rolling_sum += i

print(rolling_sum) # 872187
