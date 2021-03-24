def triple_finder():
    for i in range(1, 1000):
        for j in range(1, 1000):
            for k in range(1, 1000):
                if i + j + k == 1000 and i**2 + j**2 == k**2:
                    return i * j * k

print(triple_finder()) # 31875000