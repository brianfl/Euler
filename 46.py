prime_list = set()
length = 1000*10
sq_list = set(i**2 for i in range(1, int(length**.5)))
prime_list.add(2)

for i in range(3,length ):
    counter = 0
    for j in range(2, int(i**.5)+1):
        if i % j == 0:
            counter += 1
    if counter == 0:
        prime_list.add(i)

odd_comps = set(i for i in range(3, length) if i%2 != 0) - prime_list

target_num = 0

for number in odd_comps:
    ticker = 0
    for prime in prime_list:
        if ticker > 0:
            break
        for sq in sq_list:
            if prime + 2*(sq) == number:
                ticker += 1
                break
    if ticker == 0:
        target_num = number
        break

print(target_num) # 5777
