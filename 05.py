'''

Simpler to just do the math than iterating. Break each number from 1 to 20 into its prime components.
The find the maximum times each unique prime occurs in any of the numbers.
Include the prime that number of times.

For instance, 9 is ( 3 * 3 ) and 18 is ( 3 * 3 * 2 ), both of which are the most
number of times 3 shows up.

So include 3 twice. Cheaper to do so using 9 since we already get a 2 from other numbers.

This works since primes can be recombined to form any of the numbers, but you need
to have enough of the primes to actually do so. You can use 5 and 2 to make 10, but
you need to include another 2 to make 20, for instance.

'''

print(16 * 17 * 5 * 13 * 9 * 11 * 19 * 7) # 232792560

# print(
#     (2 * 2 * 2 * 2) * (17) * (5) * (13) * (3 * 3) * (11) * (19) * (7)
# )