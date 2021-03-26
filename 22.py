with open ("names.txt", "r") as names:
    list1 = names.read().split(",")

list2 = []
for name in list1:
    cool_name = name.strip("\"")
    list2.append(cool_name)

list2 = sorted(list2)
score_dict = {}
char_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for index, value in enumerate(char_string):
    score_dict[value] = index + 1

s = 0

for index, value in enumerate(list2):
    g = 0
    for c in value:
        g += score_dict[c]
    s += g * (index + 1)

print(s) # 871198282