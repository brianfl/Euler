with open('matrix.txt', 'r') as m:
    n = m.read().split('\n')
    matrix = [i.split(',') for i in n]
    del matrix[-1]

for index1, value1 in enumerate(matrix):
    for index2, value2 in enumerate(value1):
        matrix[index1][index2] = int(value2)

nodes = {}

# first, create a dictionary that labels each node with its connections and their costs with other nodes

node_val = 0
for row_ind, row in enumerate(matrix):
    for item_ind, item in enumerate(row):
        if row_ind == 0:
            if item_ind == 0:
                nodes[node_val] = {1:row[1], len(row): matrix[row_ind+1][item_ind]}
            elif item_ind == len(row)-1:
                nodes[node_val] = {node_val-1: matrix[row_ind][item_ind-1], node_val+len(row): matrix[row_ind+1][item_ind]}
            else:
                nodes[node_val] = {node_val-1: matrix[row_ind][item_ind-1], node_val+len(row): matrix[row_ind+1][item_ind], node_val+1: matrix[row_ind][item_ind+1]}
        elif row_ind == len(matrix)-1:
            if item_ind == 0:
                nodes[node_val] = {row_ind*len(row)+1:row[1], (row_ind-1)*len(row): matrix[row_ind-1][item_ind]}
            elif item_ind == len(row)-1:
                nodes[node_val] = {node_val-1: matrix[row_ind][item_ind-1], node_val-len(row): matrix[row_ind-1][item_ind]}
            else:
                nodes[node_val] = {node_val-1: matrix[row_ind][item_ind-1], node_val-len(row): matrix[row_ind-1][item_ind], node_val+1: matrix[row_ind][item_ind+1]}
        else:
            if item_ind == 0:
                nodes[node_val] = {node_val+1:row[1], node_val-len(row): matrix[row_ind-1][item_ind], node_val+len(row): matrix[row_ind+1][item_ind]}
            elif item_ind == len(row)-1:
                nodes[node_val] = {node_val-1: row[-2], node_val-len(row): matrix[row_ind-1][item_ind], node_val+len(row): matrix[row_ind+1][item_ind]}
            else:
                nodes[node_val] = {node_val-1: row[item_ind-1], node_val+1: row[item_ind+1], node_val-len(row): matrix[row_ind-1][item_ind], node_val+len(row): matrix[row_ind+1][item_ind]}

        node_val += 1

# Dijkstra implementation

dist_stat = {}

for node in nodes:

    # set the first node to distance zero, and every other node to distance inf

    if node==0:
        dist_stat[node] = [0, 't']
    else:
        dist_stat[node] = [10**100, 't']

curr_pos = 0

while True:
    node_val = curr_pos
    for connected_node in nodes[node_val]:
        # for every node connected to the current node,
        # if the path through the current node is less than the tentative distance, update the distance

        dist = dist_stat[node_val][0] + nodes[node_val][connected_node]
        if dist < dist_stat[connected_node][0]:
            dist_stat[connected_node][0] =  dist

    # indicate that the current node is completed
    dist_stat[node_val][1] = 'p'    

    # then, find the node closest to the origin that is not completed. Start again from there      
    min_val = 10**100
    min_node = -1
    for node in dist_stat:
        if dist_stat[node][1] == 't' and dist_stat[node][0] < min_val:
            min_val = dist_stat[node][0]
            min_node = node
    if min_node == -1:
        # if no such node exists, we're done
        break
    else:
        curr_pos = min_node


print(dist_stat[max(dist_stat)][0]+matrix[0][0]) # 425185

"""

Using Dijkstra to traverse the matrix.

Have to be a bit creative in defining the graph, since it is bidirectional
but each way has a different cost.

"""