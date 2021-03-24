fib_list = [1, 2]

while fib_list[-1] < 4000000:
    fib_list.append( fib_list[-1] + fib_list[-2] )

even_fibs = [i for i in fib_list if i % 2 == 0]

print(sum(even_fibs)) # 4613732