with open('matrix.txt', 'r') as m:
    n = m.read().split('\n')
    matrix = [i.split(',') for i in n]
    del matrix[-1]

for index1, value1 in enumerate(matrix):
    for index2, value2 in enumerate(value1):
        matrix[index1][index2] = int(value2)

row_pos = len(matrix)-1
ind_pos = len(matrix[row_pos])-1

while row_pos >= 0:
    while ind_pos >= 0:
        below_value = 10**7
        right_value = 10**7

        try:
            below_value = matrix[row_pos+1][ind_pos]
        except:
            pass
        
        try:
            right_value = matrix[row_pos][ind_pos+1]
        except:
            pass
        if below_value != 10**7 or right_value != 10**7:
            matrix[row_pos][ind_pos] += min([below_value, right_value])
        ind_pos -= 1
    row_pos -= 1
    ind_pos = len(matrix[row_pos])-1

print(matrix[0][0]) # 427337

"""

Same concept as the previous pathway problems.

Although I realized that 0,0 will always just be the answer,
no need to walk back down the path.

"""