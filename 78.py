d1 = {0:1, 1:1, 2:2, 3:3}
pent_nums = []

for i in range(1, 100001):
    val1 = ((3*(i**2))-i)/2
    val2 = ((3*((-i)**2))+i)/2
    pent_nums.append(val1)
    pent_nums.append(val2)

for n in range(4, 100001):
    ite = 0
    p_t = d1[n-pent_nums[ite]]
    step = 1
    stop = False
    rolling_sum = 0
    while not stop:
        if step == 1 or step == 2:
            rolling_sum += p_t
            step += 1
        elif step==3:
            rolling_sum -= p_t
            step += 1
        else:
            rolling_sum -= p_t
            step = 1
        ite += 1

        try:
            if d1[n-pent_nums[ite]] > 0:
                p_t = d1[n-pent_nums[ite]]
        except:
            stop = True
    d1[n] = rolling_sum

for i in d1:
    if d1[i]%1_000_000==0:
        target = i
        break

print(target) # 55374

"""

Reusing the code from 76 since it's the same concept.
Not the quickest but if you use a high enough value eventually
you find the number you need.

"""
