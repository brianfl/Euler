bound =  int(600851475143**.5) + 2

number_list = set(i for i in range(2,bound))

p = 2
p_list = []

while p != max(number_list):
    mult_list = set( i for i in range(p, bound, p))
    mult_list.remove(p)

    number_list = number_list - mult_list
    p_list.append(p)
    j = 0

    while j == 0:
        for i in number_list:
            if i not in p_list:
                j = i
                break
    p = j
    
max_fac = 0

for i in number_list:
    if 600851475143 % i == 0 and i > max_fac:
        max_fac = i

print(max_fac) # 6857

# On my machine, this runs in about 15 seconds in Python 2.7.18.
# But when I run it on 3.8.5, I don't even know if it terminates.
# WTF? Investigate at some point...