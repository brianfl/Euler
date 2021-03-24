three_digits = [i for i in range(100, 1000)][::-1]

dromes = []

for i in three_digits:
    for j in three_digits:
        product = j * i
        if str(product)[0:3] == str(product)[3:][::-1]:
            dromes.append(product)

print(max(dromes)) # 906609
