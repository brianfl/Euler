sum_of_squares = 0
sum1 = 0

for i in range(1,101):
    sum_of_squares += i**2
    sum1 += i

print( sum1 ** 2 - sum_of_squares ) # 25164150