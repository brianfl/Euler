with open ("cipher.txt", "r") as cipher:
    l1 = cipher.read().split(',')

sum1 = 0

index = 0
stop = False

while not stop:
    for i in range(97, 122):
        for j in range(97, 122):
            for k in range(97, 122):
                l2 = ''
                step = 0
                for ch in l1:
                    if step == 0:
                        l2 += chr(int(ch)^int(i))
                        step += 1
                    elif step == 1:
                        l2 += chr(int(ch)^j)
                        step += 1
                    elif step == 2:
                        l2 += chr(int(ch)^k)
                        step = 0
                if 'Euler' in l2:
                    for l in l2:
                        sum1 += ord(l)
                    stop = True

print(sum1) # 129448