divisor_dict = {}

for number in range(1, 10001):
    list_divs = []
    for potential in range(1, number):
        if number % potential == 0:
            list_divs.append(potential)
    divisor_dict[number] = list_divs

pairs_sum = set()

for key in divisor_dict:
    for key2 in divisor_dict:
        if sum(divisor_dict[key]) == key2 and sum(divisor_dict[key2]) == key and key != key2:
            pairs_sum.add(key)
            pairs_sum.add(key2)

print(sum(pairs_sum)) # 31626
    
