import math
rolling_sum = 0
skipped = 0
number = 3
while skipped < 100000*5:
    s = str(number)
    fac_sum = 0
    for i in s:
        fac_sum += math.factorial(int(i))
    if fac_sum == number:
        rolling_sum += number
    else:
        skipped += 1
    number += 1

print(rolling_sum) # 40730

# Not pretty, but if we haven't hit a valid number in half a million numbers, we're probably done.
# Runs in a couple seconds anyway.