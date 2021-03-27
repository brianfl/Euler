import math
permutation_list = [0,1,2,3,4,5,6,7,8,9]

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
    list_perms.append(sum1)

print(list_perms[-1]) # 2783915460

"""

Pandita's algorithm for lexicographic generation

"""
