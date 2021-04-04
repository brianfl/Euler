lychrels = 0

for i in range(0, 10001):
    s = str(i)
    n = i
    indicator = 0
    for j in range(0, 50):
        n = n + int(s[::-1])
        s = str(n)
        l = len(s)
        if l % 2 == 0:
            p1 = s[0:int(l/2)]
            p2 = s[int(l/2):][::-1]
        else:
            p1 = s[0:int(l/2)+1]
            p2 = s[int(l/2):][::-1]
        if p1 == p2:
            indicator += 1
            break
    
    if indicator == 0:
        lychrels += 1

print(lychrels) # 249