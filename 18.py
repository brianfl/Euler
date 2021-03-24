import copy

str1 = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

array1 = str1.split('\n')
del array1[0]
del array1[-1]

for index, value in enumerate(array1):
    array1[index] = value.split(' ')
    array1[index] = [int(i) for i in array1[index]]

array2 = copy.deepcopy(array1[::-1]) # Python passes lists by reference by default. Who knew?

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

print(rolling_sum) # 1074

"""

For future reference, what I'm doing here is walking backwards through the list
and rewriting values to be the original value plus the value of the largest child.
This is because the weight of each value is not just what it adds to the sum,
but what its children will add to the sum. Walking backwards will 
rewrite each original value to it's true "present value".
Then you just have to choose the largest value available to you at each step.

"""