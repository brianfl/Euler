import math
lattice_size = 20

# list_paths = set()

# for i in range(1, 2**(lattice_size * 2)):
#     binary = bin(i-1)
#     string = binary[2:]
#     missing = lattice_size * 2 - len(string)
#     string = missing * str(0) + string
#     if  not(string.count('1') > lattice_size or string.count('0') > lattice_size):
#         list_paths.add(string)
#     if len(list_paths) % 1000 == 0 and len(list_paths) != 0:
#         print(len(list_paths))

numerator = ( math.factorial(lattice_size * 2) )
denominator = 1
for i in range(1, lattice_size + 1):
    denominator = denominator * (i ** 2)

print(numerator/denominator) # 137846528820

"""
So the commented out function works, it's just way too slow for large numbers.
However I was able to use it to explore the answers to smaller grids, like 2x2 to 6x6.
The process reminded me of permutations and combinations, so I experimented with
different possible factorial functions.
Eventually I stumbled on to the formula (where pi is the product function)

y =     (2 * x)!
    --------------------
    pi( i ** 2) from 1 to x

I don't really know where this formula comes from, but it works.
The numerator is probably related to the perm/comb factorials.
The denominator seems to reflect that each additional row/column
added compounds the complexity of the previous grid?
Worth investigating.

"""