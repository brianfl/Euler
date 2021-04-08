sq_odd_nums_d = {}

for i in range(1, 300, 2):
    sq_odd_nums_d[i**2] = True

mult_six_d = {}
mult_oct_d = {}

for i in range(0, 600, 6):
    if i != 0:
        mult_six_d[(i-1)**2] = True
        mult_oct_d[(i-2)**2] = True

sq_nums_d = {}

for i in range(1, 300):
    sq_nums_d[i**2] = True

mult_four_d = {}

for i in range(0, 300, 4):
    if i != 0:
        mult_four_d[(i-1)**2] = True

mult_ten_d = {}

for i in range(10, 700, 10):
    if i!=10:
        mult_ten_d[(i-3)**2] = True

list_cycles = []

tri_nums = []
pent_nums = []
sq_nums = []
hex_nums = []
hep_nums = []
oct_nums = []

for i in range(0, 150):
    tri_nums.append(int(i*(i+1)/2))
    pent_nums.append(int(i*(3*i-1)/2))
    sq_nums.append(int(i**2))
    hex_nums.append(int(i*(2*i-1)))
    hep_nums.append(int(i*(5*i-3)/2))
    oct_nums.append(int(i*(3*i-2)))

l1 = [tri_nums, pent_nums, sq_nums, hep_nums, hex_nums, oct_nums]

for ind, value in enumerate(l1):
    new_list =[]
    for j in value:
        if len(str(j)) == 4:
            last2 = str(j)[-2:]
            count = 0
            for k in l1:
                for item in k:
                    if k != value:
                        if str(item)[0:2] == last2:
                            count += 1
            if not count == 0:
                new_list.append(j)
    l1[ind] = new_list

for index, lyst in enumerate(l1):
    valid_nums = []
    for item in lyst:

        l_count = 0
        r_count = 0

        for lost in l1:
            if lost != lyst:
                for ytem in lost:
                    if str(ytem)[2:] == str(item)[0:2]:
                        r_count += 1
                    if str(ytem)[:2] == str(item)[2:]:
                        l_count += 1
        if l_count > 0 and r_count > 0:
            valid_nums.append(item)
    l1[index] = valid_nums

def cycle(value, lst, chain, rollin):
    r = rollin
    ch = chain
    if ch == 0:
        r = [value]
    elif ch > 0:
        r.append(value)
    
    if len(r) == 6:
        return r

    for index, lyst in enumerate(l1):
        if lyst != lst:
            for item in lyst:
                stopper = 0
                count = 0
                if str(value)[2:] == str(item)[0:2]:
                    if len(r) == 5:
                        if str(item)[2:] == str(r[0])[0:2]:
                            stopper += 1
                            nitem = item
                            nlist = lyst
                    else:
                        stopper += 1
                        nitem = item
                        nlist = lyst
                if stopper > 0:
                    break
            if stopper > 0:
                break
    if stopper > 0:
        return cycle(nitem, nlist, ch+1, r)
    else:
        return False

for l in l1:
    for item in l:
        r = cycle(item, l, 0, [])
        if r != False:
            list_cycles.append(r)

def jvn():
    for cycle in list_cycles:
        num1, num2, num3, num4, num5, num6 = cycle[0], cycle[1], cycle[2], cycle[3], cycle[4], cycle[5]
        l6 = [num1, num2, num3, num4, num5, num6]
                
        tri, pent, sq, hx, hp, oc = 0, 0, 0, 0, 0, 0
        none = 0
        for item in l6:
            t, s, p, h, h2, o = 0, 0, 0, 0, 0, 0
            try:
                if sq_odd_nums_d[(1+8*item)]:
                    t += 1
            except:
                pass

            try:
                if mult_six_d[(1+24*item)]:
                    p += 1
            except:
                pass

            try:
                if sq_nums_d[(item)]:
                    s += 1
            except:
                pass

            try:
                if mult_four_d[(1+8*item)]:
                    h += 1
            except:
                pass

            try:
                if mult_ten_d[(9+40*item)]:
                    h2 += 1
            except:
                pass

            try:
                if mult_oct_d[(4+12*item)]:
                    o += 1
            except:
                pass
                
            if s == 0 and p == 0 and t == 0 and h == 0 and h2 == 0 and o == 0:
                none += 1
                no_good[item] = True
            else:
                sq += s
                pent += p
                tri += t
                hx += h
                hp += h2
                oc += o
            
        if none != 0:
            pass
        else:
            if tri != 0 and pent != 0 and sq != 0 and hx != 0 and hp != 0 and oc != 0:
                return num1 + num2 + num3 + num4 + num5 + num6 
    
print(jvn()) # 28684

"""

Implemented a much better way to generate cycles of numbers.
Cut down execution greatly.

"""


