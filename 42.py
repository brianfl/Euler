with open ('words.txt', 'r') as text:
    list1 = text.read().split(",")

max_len = 0

for index, value in enumerate(list1):
    n_val = value.strip('\"')
    list1[index] = n_val
    if len(n_val) > max_len:
        max_len = len(n_val)

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

tri_nums = []

max_score = max_len * 26

max_int = ( -1 + (1 + 8*max_score)**.5)/2 # By the quadratic formula, the number of iterations to achieve the max triangle number possible.

for i in range(1, int(max_int)+1):
    tri_nums.append(
        .5 * (i) * (i + 1)
    )

counter = 0

for word in list1:
    score = 0
    
    for character in word:
        ind = chars.find(character)
        score += ind + 1

    if score in tri_nums:
        counter += 1

print(counter) # 162    
