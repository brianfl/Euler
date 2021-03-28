m = set()

for i in range(2, 101):
    for j in range(2, 101):
        m.add(i**j)
        
print(len(m)) # 9183
