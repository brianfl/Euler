import random
squares = [0 for i in range(0, 40)]
state = 0
num_rolls = 1_000_000*3
doubles = 0

chest = ['0' for i in range(0, 14)]
chest.append('GO')
chest.append('JAIL')
random.shuffle(chest)

chance = ['0' for i in range(0, 6)]
chance.append('GO')
chance.append('JAIL')
chance.append('C1')
chance.append('E3')
chance.append('H2')
chance.append('R1')
chance.append('R')
chance.append('R')
chance.append('U')
chance.append('3')
random.shuffle(chance)

for roll in range(0, num_rolls):
    d_1 = random.randint(1, 4)
    d_2 = random.randint(1, 4)
    if d_1 == d_2:
        doubles += 1
    else:
        doubles = 0
    
    land = d_1 + d_2
    state += land

    if doubles == 3:
        state = 10
        doubles = 0

    if state>=40:
        state -= 40

    if state == 30:
        state = 10

    elif state == 2 or state == 17 or state == 33:
        card = chest[0]
        if card == '0':
            pass
        elif card == 'GO':
            state = 0
        elif card == 'JAIL':
            state = 10
        chest.pop(0)
        chest.append(card)
    
    elif state == 7 or state == 22 or state == 36:
        card = chance[0]
        if card == '0':
            pass
        elif card == 'GO':
            state = 0
        elif card == 'JAIL':
            state = 10
        elif card == 'C1':
            state = 11
        elif card == 'E3':
            state = 24
        elif card == 'H2':
            state = 39
        elif card == 'R1':
            state = 5
        elif card == 'R':
            if state == 7:
                state = 15
            elif state == 22:
                state = 25
            elif state == 36:
                state = 5
        elif card == 'U':
            if state == 7:
                state = 12
            elif state == 22:
                state = 28
            elif state == 36:
                state = 12
        elif card == '3':
            state -= 3

        chance.pop(0)
        chance.append(card)
    
    squares[state] += 1

squares = [i/num_rolls for i in squares]

z = []

for index, value in enumerate(squares):
    z.append((value, index))

s_1 = ''

z = sorted(z, reverse=True)

for i in range(0, 3):
    s_1 += str((z[i][1]))

print(s_1) # 101524

"""

So, this isn't the most elegant answer, and I'm sure there is an 'analytical' solution.
And I can't even be sure it prints the right answer all of the time.
But it's good enough!

"""

