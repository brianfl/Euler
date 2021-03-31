def is_prime(number):
    counter = 0
    for i in range(2, int(number**.5)+1):
        if number % i == 0:
            counter += 1
    if counter == 0 and number != 1:
        return True
    return False

rolling_sum = 0

for i in range(10, 100000*8):
        s = str(i)
        l1 = ['0','2','4','5','6','8']
        if not (len(s) > 2 and s[0] in l1 or s[-1] in l1):
            if is_prime(i):
                not_prime = 0

                s_c = str(i)
                for k in range(0,2):
                    if k == 0:
                        while len(s_c) > 1:
                            s_c = s_c[1:]
                            if not is_prime(int(s_c)):
                                not_prime += 1
                    else:
                        while len(s) > 1:
                            s = s[:-1]
                            if not is_prime(int(s)):
                                not_prime += 1
                if not_prime == 0:
                    rolling_sum += i

print(rolling_sum) # 748317

