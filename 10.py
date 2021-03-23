def prime_test(number):
    for i in range(2, int(number**.5) + 1):
        if number % i == 0:
            return False
    return True

prime_list = [2]

number = 2
while prime_list[-1] < 2000000:
    number += 1
    if prime_test(number):
        prime_list.append(number)

del prime_list[-1]

print(sum(prime_list)) # 142913828922
