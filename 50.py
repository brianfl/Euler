list_primes = [2]

for i in range(3, 5000):
    counter = 0
    for j in list_primes:
        if j > int(i**.5) + 1:
            break
        if i % j == 0:
            counter += 1
            break
    if counter == 0:
        list_primes.append(i)


section_length = len(list_primes)
index = 0

target = 0

while section_length > 1:
    section = list_primes[index:section_length+index]
    sum1 = 0
    for i in section:
        sum1 += i
    counter = 0
    if sum1 < 1000000:
        for j in range(2, int(sum1**.5)+1):
            if sum1 % j == 0:
                counter += 1
        if counter == 0:
            target = sum1
            break
    index += 1
    if index + section_length > len(list_primes):
        index = 0
        section_length -= 1

print(target) # 997651