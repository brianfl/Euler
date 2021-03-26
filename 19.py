import copy
list_days = []
firsts = []

for i in range(1901, 2001):
    if i % 4 == 0:
        for j in range(1, 367):
            list_days.append(False)
        firsts.append([False for k in range(1, 367)])
    else:
        for j in range(1, 366):
            list_days.append(False)
        firsts.append([False for k in range(1, 366)])

for year in firsts:
    year[0] = True
    year[31] = True
    month_indices = [59, 89, 120, 150, 181, 212, 242, 273, 303, 334]
    if len(year) == 366:
        offset = 1
    else:
        offset = 0
    for value in month_indices:
        year[value + offset] = True

re_firsts = []

for year in firsts:
    for day in year:
        re_firsts.append(day)

pos = 6

while pos < len(list_days):
    list_days[pos] = True
    pos += 7

counter = 0
for index, value in enumerate(list_days):
    if value == True and re_firsts[index] == True:
        counter += 1

print(counter) # 171

"""

After doing all this I realized there are 1200 months in a hundred year period,
and 1200 * (1/7) = 171.49. So you could have just figured this out with
frequencies.

"""