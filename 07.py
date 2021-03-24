prime_list = [2]
current_number = 2

while len(prime_list) < 10001:
    current_number += 1
    counter = 0
    for i in prime_list:
        if current_number % i != 0:
            counter += 1
    if counter == len(prime_list):
        prime_list.append(current_number)

print(prime_list[-1]) # 104743

# Slow. A litte over a minute. Can optimize.