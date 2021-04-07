import math
prime_list = {2:True}

for i in range(3, 8500):
    counter = 0
    for j in prime_list:
        if i % j == 0:
            counter += 1
            break
        if j > int(i**.5) + 1:
            break
    if counter == 0:
        prime_list[i] = True

def primecheck(item):
    counter = 0
    for i in range(2, int(item**.5)+1):
        if item % i == 0:
            counter += 1
            break
    if counter == 0:
        return True
    return False

combos = {}

def combocheck(k1, k2):
    list1 = [k1, k2]
    try:
        var1 = combos[tuple(sorted(list1))]
        return var
    except:
        list2 = []
        duplicate = False
        count = 0   
        for index, item in enumerate(list1):
            if list1.count(item) > 1:
                return False
            for index2, item2 in enumerate(list1):
                if index != index2:
                    var3 = int(str(item)+str(item2))
                    try:
                        if prime_list[var3]:
                            count += 1
                    except:
                        if primecheck(var3):
                            count += 1
        if count == 2:
            combos[tuple(sorted(list1))] = True
            return True
        combos[tuple(sorted(list1))] = False
        return False

def funcy():
    for key1 in prime_list:
        for key2 in prime_list:
            if combocheck(key1, key2):
                for key3 in prime_list:
                    if combocheck(key1, key3) and combocheck(key2, key3):
                        for key4 in prime_list:
                            count = 0
                            l1 = [key1, key2, key3]
                            for item in l1:
                                if combocheck(key4, item):
                                    count += 1
                            if count == 3:
                                for key5 in prime_list:
                                    count = 0
                                    l2 = [key1, key2, key3, key4]
                                    for item in l2:
                                        if combocheck(key5, item):
                                            count += 1
                                    if count == 4:
                                        return key1 + key2 + key3 + key4 + key5
    return False

print(funcy()) # 26033

"""

Even after spending some time trying to optimize this it 
still runs in over 4 minutes.

Obviously room for improvement. But I'll probably have to 
rewrite the whole thing.

Worth learning a better way to do this and coming back to it.

"""
            

