import math
permutation_list = [0,1,2,3,4,5,6,7,8,9]

stop = False

list_perms = []

divisors = [2, 3, 5, 7, 11, 13, 17]

for i in range(1, 1000000*3 ):
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
    div_count = 0

    for k in range(2, 9):
        if int(sum1[k-1:k+2]) % divisors[k-2] == 0:
            div_count += 1
    if div_count == 7:
        list_perms.append(int(sum1))

print(sum(list_perms)) # 16695334890

"""

Reusing the algorithm from 24.

"""
