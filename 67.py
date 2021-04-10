import copy

with open('triangle.txt', 'r') as triangle:
    tri = triangle.read()

array1 = tri.split('\n')

del array1[-1]

for index, value in enumerate(array1):
    array1[index] = value.split(' ')
    array1[index] = [int(i) for i in array1[index]]

array2 = copy.deepcopy(array1[::-1]) 

for index1, value in enumerate(array2):
    if index1 == 0:
        pass
    else:
        for index2, number in enumerate(value):
            children = [array2[index1-1][index2], array2[index1-1][index2+1]]
            maxchild = max(children)
            array2[index1][index2] = number + maxchild

list_indices = []

array2 = array2[::-1]

current_pos = 0

for index1, value in enumerate(array2):
    if index1 == len(array2)-1:
        list_indices.append(current_pos)
    else:
        list_indices.append(current_pos)
        children = [array2[index1+1][current_pos], array2[index1+1][current_pos+1]]
        maxchild = max(children)
        if children[0] == maxchild:
            pass
        else:
            current_pos += 1

rolling_sum = 0
for index1, value in enumerate(array1):
    rolling_sum += value[list_indices[index1]]

print(rolling_sum) # 7273

"""
Barely had to change anything from problem 18.
"""