sections = []
max_16 = 0
len1 = 11
for a in range(1, len1):
    for b in range(1, len1):
        if b!= a:
            for c in range(1, len1):
                if c!=a and c!=b:
                    for d in range(1, len1):
                        if d!=c and d!=b and d!=a:
                            for e in range(1, len1):
                                if e!=d and e!=c and e!=b and e!=a:
                                    for f in range(1, len1):
                                        if f!=d and f!=e and f!=b and f!=c and f!=a:
                                            for g in range(1, len1):
                                                if not any([g==f, g==e,g==d,g==c,g==b,g==a]) and e+f+g==a+b+c: # including the second condition cuts down runtime significantly
                                                    for h in range(1, len1):
                                                        if not any([h==g,h==g,h==f,h==e,h==d,h==c,h==b,h==a]):
                                                            for i in range(1, len1):
                                                                if not any([i==h,i==g,i==f,i==e,i==d,i==c,i==b,i==a]):
                                                                    for j in range(1, len1):
                                                                        if not any([j==i,j==h,j==g,j==f,j==e,j==d,j==c,j==b,j==a]):

                                                                            var1 = a+b+c
                                                                            var1s = str(a)+str(b)+str(c)
                                                                            var2 = d+c+f
                                                                            var2s = str(d)+str(c)+str(f)
                                                                            var3 = e+f+g
                                                                            var3s = str(e)+str(f)+str(g)
                                                                            var4 = j+g+h
                                                                            var4s = str(j)+str(g)+str(h)
                                                                            var5 = i+h+b
                                                                            var5s = str(i)+str(h)+str(b)
                                                                            if var1 == var2 and var2 == var3 and var3 == var4 and var4==var5:
                                                                                if var1s not in sections and var2s not in sections and var3s not in sections and var4s not in sections and var5s not in sections:
                                                                                    l1 = [a,d,e,j,i]
                                                                                    start = l1.index(min(l1))

                                                                                    if start==0:
                                                                                        str1 = var1s+var2s+var3s+var4s+var5s
                                                                                    elif start ==1:
                                                                                        str1 = var2s+var3s+var4s+var5s+var1s
                                                                                    elif start == 2:
                                                                                        str1 = var3s+var4s+var5s+var1s+var2s
                                                                                    elif start == 3:
                                                                                        str1 = var4s+var5s+var1s+var2s+var3s
                                                                                    elif start==4:
                                                                                        str1=var5s+var1s+var2s+var3s+var4s
                                                                                    
                                                                                    if len(str1)==16 and int(str1)>max_16:
                                                                                        max_16=int(str1)
                                                                                sections.append(var1s)
                                                                                sections.append(var2s)
                                                                                sections.append(var3s)
                                                                                sections.append(var4s)
                                                                                sections.append(var5s)

print(max_16) # 6531031914842725
