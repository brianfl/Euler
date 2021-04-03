list1 = []
list_primes = set()
list_primes.add(2)
start = 10000*7
stop = start+10000

for num in range(2, stop):
    counter = 0
    for num2 in range(2, int(num**.5)+1):
        if num % num2 == 0:
            counter += 1
    if counter == 0:
        list_primes.add(num)

for i in range(start, stop):
    p_count = 0
    for j in range(2, i):
        if i % j == 0:
            if j in list_primes:
                p_count += 1
    if p_count == 4:
        list1.append(i)
print(list1)
for i in list1:
    if i-1 in list1 and i-2 in list1 and i-3 in list1:
        print(i-3)

# Incomplete. Slow. Getting there. 

