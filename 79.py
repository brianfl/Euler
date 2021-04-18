with open('keylog.txt', 'r') as log:
    l1 = log.read().split('\n')
    del l1[-1]

s1 = ''

for i in l1:
    for j in i:
        s1 += j

set1 = set()

for i in s1:
    set1.add(int(i))

import math
permutation_list = list(set1)

stop = False

list_perms = []

for i in range(1, 1000000):
    for index, value in enumerate(permutation_list):
        try:
            if permutation_list[index] < permutation_list[index+1]:
                current_index = index
        except:
            pass
    for index2, value2 in enumerate(permutation_list):
        if value2 > permutation_list[current_index] and index2 > current_index:
            swap_large = value2
            large_index = index2
    swap_small = permutation_list[current_index]

    permutation_list[current_index] = swap_large
    permutation_list[large_index] = swap_small

    rev = permutation_list[current_index + 1:][::-1]
    permutation_list[current_index + 1:] = rev
    sum1 = ''
    for j in permutation_list:
        sum1 += str(j)
    if len(list_perms)>0:
        if sum1 == list_perms[-1]:
            break
        else:
            list_perms.append(sum1)
    else:
        list_perms.append(sum1)

for item in l1:
    for perm in list_perms:
        p = perm
        s = ''
        for char in p:
            if char in item:
                 s += char
        if item not in s:
            list_perms.remove(perm)

print(list_perms[0]) # 73162890

"""

Another copy of the lexicographic permutation algorithm.

Much easier to just do this problem by hand, although I'm
sure a better implementation is possible.

"""