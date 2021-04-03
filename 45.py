target_num = 0
j = 0

while target_num == 0:
    pent_ind = float((1 + ( 1 + 24*j*(2*j-1))**.5)/6)
    tri_ind = float((-1 + (1+8*j*(2*j-1)))/2)
    if pent_ind.is_integer() and tri_ind.is_integer():
        num = j*(2*j-1)
        if num != 1 and num != 40755:
            target_num = num
    j += 1

print(target_num) # 1533776805
 
"""

I had a brute force solution, but it was a bit over a minute.
By solving for the index values of pentagon and triangle numbers
in terms of the index value of the hexagon numbers,
the formulas in pent_ind and tri_ind pop out of the quadratic equation.
Basically those variables will only be integers if j is a valid index
for a pentagon number and triangle number as well.

"""