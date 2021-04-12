prime_list = []

bound = 10000000

for num in range(int(bound**.5)-1000, int(bound**.5)+1000):
    count=0
    for i in range(2, int(num**.5)+1):
        if num%i==0:
            count += 1
            break
    if count==0:
        prime_list.append(num)

phin_dict = {}

for p1 in prime_list:
    for p2 in prime_list:
        if p1!=p2 and p1*p2<bound:
            t1 = tuple(sorted([p1,p2]))
            try:
                if phin_dict[t1]!=0:
                    pass
            except:
                prod = 1
                for el in t1:
                    prod *= 1-1/el
                phin_dict[t1] = int(round(prod*p1*p2, 0))

perm_dict = {}

for i in phin_dict:
    s = str(phin_dict[i])
    p = str(i[0]*i[1])

    count = 0
    for k in s:
        if s.count(k)!=p.count(k):
            count += 1
    for k in p:
        if s.count(k)!=p.count(k):
            count += 1
    
    if count==0:
        perm_dict[i] = phin_dict[i]

l1 = {}

for i in perm_dict:
    phi_n = i[0]*i[1]/perm_dict[i]
    l1[phi_n] = i[0]*i[1]

target = l1[min(l1)]

print(target) # 8319823
