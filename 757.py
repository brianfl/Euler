s1 = set()

for i in range(1, 4000):
    val = i*(i+1)
    sum = 0
    multiple = val*2
    incr = 1
    while True:
        sum += multiple*incr
        if sum > 10**14:
            break
        else:
            incr += 1
            s1.add(sum)

print(len(s1))

"""

First, calculated some stealthy numbers.
From OEIS, found they were "bipronic" numbers, or two pronic numbers multiplied.
Some inspection revealed you can form bipronics by multiplying a pronic by two
and repeatedly adding multiples? I don't have a good grasp on why this happens.

So calculate a bunch of pronics, multiply it by two, then keep adding that value's multiples (which are now bipronics).
Use sets to take care of the duplicates.

This solution is slow (about a minute on my machine) and takes a lot of memory.

"""