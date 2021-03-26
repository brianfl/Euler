abundant_numbers = []
can_form_abundant = set()

s = 0

for i in range(1, 28124):
    t = 0
    for j in range(1, i):
        if i % j == 0:
            t += j
    if t > i:
        abundant_numbers.append(i)
        for k in abundant_numbers:
            can_form_abundant.add( i + k )


nums = set(j for j in range(1, 28124))

cannot_form_abundant = nums - can_form_abundant

print(sum(cannot_form_abundant)) # 4179871