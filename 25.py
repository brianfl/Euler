n_2 = 1
n_1 = 1
index = 2
stop = False

while not stop:
    index += 1
    fib = n_1 + n_2
    str_fib = str(fib)
    if len(str_fib) == 1000:
        stop = True
    n_1 = n_2
    n_2 = fib

print(index) # 4782