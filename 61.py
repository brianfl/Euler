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

no_good = {}

def tbreak(item):
    try:
        if no_good[item]:
            return True
    except:
        return False

def jvn():
    for n1 in range(11, 99):
     for n2 in range(11, 99):
      num1 = int(str(n1)+str(n2))
      if tbreak(num1) == False:
       for n3 in range(11, 99):
         num2 = int(str(n2) + str(n3))
         if tbreak(num2) == False:
          for n4 in range(11, 99):
           num3 = int(str(n3)+str(n4))
           if tbreak(num3) == False:
            for n5 in range(11, 99):
             num4 = int(str(n4)+str(n5))
             if tbreak(num4)==False:
              for n6 in range(11, 99):
               num5 = int(str(n5)+str(n6))
               num6 = int(str(n6)+str(n1))
               if tbreak(num5)==False and tbreak(num6)==False:
            
                    l1 = [num1, num2, num3, num4, num5, num6]

                    stop = 0
                    for i in l1:
                        if l1.count(i)>1:
                            stop += 1
                            break
                    if stop == 0:
                        if num1 % 1000 != num1 and num2 % 1000 != num2 and num3%1000 != num3 and num4%1000!=num4 and num5%1000!=num5 and num6%1000!=num6:
                            
                            tri, pent, sq, hx, hp, oc = 0, 0, 0, 0, 0, 0
                            none = 0
                            for item in l1:
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
                                
                            if none != 0 or num1 == 1128 or num1==1247:
                                pass
                            else:
                                if tri != 0 and pent != 0 and sq != 0 and hx != 0 and hp != 0 and oc != 0:
                                    return (num1, num2, num3, num4, num5, num6)

sum1 = 0
for i in jvn():
    sum1 += i

print(sum1) # 28684

"""

Spent a while trying to optimize this by having a better method of selecting
values to test... Getting close but not quite finished.

This is a subpar solution, over 2 minutes.

"""


