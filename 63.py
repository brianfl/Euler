list1 = []

for i in range(1, 100):
    for j in range(1, 100):
        var1 = i**j
        if len(str(var1)) == j:
            list1.append(var1)

print(len(list1)) # 49