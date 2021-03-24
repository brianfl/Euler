length_list = {}

for i in range(1, 1000000):
    number = i
    steps = 0
    while number != 1:
        if number % 2 == 0:
            number = number/2
        else:
            number = 3*number + 1
        steps += 1
    length_list[steps] = i

print(length_list[max(length_list)]) # 837799