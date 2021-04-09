l1 = [2, 3]

add = 2
step = 0

for i in range(2, 100):

    if step == 0:
        l1.append( l1[i-1]*add + l1[i-2])
        step += 1
        add += 2
    else:
        l1.append(l1[i-1] + l1[i-2])
        if step == 1:
            step += 1
        elif step == 2:
            step -= 2

sum1 = 0
for i in str(l1[99]):
    sum1 += int(i)

print(sum1) # 272