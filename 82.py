with open('matrix.txt', 'r') as m:
    n = m.read().split('\n')
    matrix = [i.split(',') for i in n]
    del matrix[-1]

for index1, value1 in enumerate(matrix):
    for index2, value2 in enumerate(value1):
        matrix[index1][index2] = int(value2)

row_pos = 0
ind_pos = len(matrix[row_pos])-2
stop = False

while not stop:

    direct_cost = matrix[row_pos][ind_pos+1]
    c_list = [direct_cost]

    if row_pos == 0:
        ind = 1
        current_lower_cost = matrix[row_pos+1][ind_pos] + matrix[row_pos+1][ind_pos+1]
        while current_lower_cost < direct_cost:

            c_list.append(current_lower_cost)
            current_lower_cost -= matrix[row_pos+ind][ind_pos+1]
            ind += 1
            current_lower_cost += matrix[row_pos+ind][ind_pos] + matrix[row_pos+ind][ind_pos+1]

        matrix[row_pos][ind_pos] = matrix[row_pos][ind_pos] + min(c_list)

    elif row_pos == len(matrix)-1:

        ind = 1
        current_upper_cost = matrix[row_pos-1][ind_pos]

        while current_upper_cost < direct_cost:

            c_list.append(current_upper_cost)
            ind += 1
            current_upper_cost += matrix[row_pos-ind][ind_pos]
        
        matrix[row_pos][ind_pos] = matrix[row_pos][ind_pos] + min(c_list)
    
    else:
        # upper search
        upper_ind = 1
        current_upper_cost =  matrix[row_pos-upper_ind][ind_pos]

        while current_upper_cost < direct_cost and row_pos - upper_ind >= 0:
            c_list.append(current_upper_cost)

            upper_ind += 1
            current_upper_cost += matrix[row_pos-upper_ind][ind_pos]

        # lower search
        lower_ind = 1
        current_lower_cost = matrix[row_pos+lower_ind][ind_pos] + matrix[row_pos+lower_ind][ind_pos+1]           

        while current_lower_cost < direct_cost and row_pos + lower_ind <= len(matrix)-1:
            c_list.append(current_lower_cost)
            current_lower_cost -= matrix[row_pos+lower_ind][ind_pos+1]
            lower_ind += 1
            try:
                current_lower_cost += matrix[row_pos+lower_ind][ind_pos] + matrix[row_pos+lower_ind][ind_pos+1]
            except:
                pass
        
        matrix[row_pos][ind_pos] = matrix[row_pos][ind_pos] + min(c_list)
    
    row_pos += 1

    if row_pos == len(matrix):
        row_pos = 0
        ind_pos -= 1
        if ind_pos == -1:
            stop = True

starts = []

for i in matrix:
    starts.append(i[0])

print(min(starts)) # 260324

"""

I could have implemented my ideas cleaner but this works.

Move backwards from the end column. For each item in the column, we're
trying to find the cheapest way to get to the next (right) column.

Usually moving directly right is the quickest, but not always. So this
algorithm searches both up and down for the cheapest way to get to the next
column.

A little tricky because sometimes the weights are included already (upwards)
and sometimes not (downwards).

"""