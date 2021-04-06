diag_list = [1]

stop = False
index = 1
number = 1
side_length = 1
total_primes = 0

while not stop:
    add_step = index*2
    for i in range(0, 4):
        number += add_step
        diag_list.append(number)
        count = 0
        for j in range(2, int(number**.5)+1):
            if number % j == 0:
                count += 1
                break
        if count == 0:
            total_primes += 1

    index += 1
    side_length += 2
    if (total_primes)/len(diag_list) < .1:
        stop = True

print(side_length) # 26241
