triangle_numbers = []

current_triangle = 0
index = 1

while current_triangle < 2_000_000:
    current_triangle += index
    triangle_numbers.append(current_triangle)
    index += 1

best_diff = 1_000_000
for num in range(len(triangle_numbers)):
    for num2 in range(len(triangle_numbers)):

        val = (triangle_numbers[num-1]*triangle_numbers[num2-1])
        if abs(val-2_000_000)<best_diff:
            best_num = num*num2
            best_diff = abs(val-2_000_000)

print(best_num) # 2772

"""

Inspection shows that the number of rectangles for g*h is equal to the g_th triangle number
multiplied by the h_th triangle number.

"""
