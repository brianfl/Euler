with open("poker.txt" , "r") as poker:
    l1 = poker.read().split("\n")
    del l1[-1]

one_wins = 0

scores = {
    '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
    'T':10,'J':11,'Q':12,'K':13,'A':14,
    'pair':15,
    'twopair':16,
    'threekind':17,
    'straight':19,
    'flush':20
}

for hand in l1:
    stop1 = False
    stop2 = False
    while not (stop1 and stop2):
        h1 = hand[0:14].split(" ")
        h2 = hand[15:].split(" ")
        an1 = ''
        an2 = ''

        count = 0
        list1 = [i[1] for i in h1]
        for j in list1:
            if j == list1[0]:
                count += 1
        if count == 5:
            an1 = 'flush'
            stop1 = True
        count = 0
        list1 = [i[1] for i in h2]
        for j in list1:
            if j == list1[0]:
                count += 1
        if count == 5:
            an2 = 'flush'
            stop2 = True

        sequence = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
        hstring = ''
        for card in h1:
            hstring += card
        for com in range(0, 9):
            seq = sequence[0+com:5+com]
            tracker = 0
            for c in seq:
                if c in hstring:
                    tracker += 1
            if tracker == 5:
                an1 = 'straight'
                stop1 = True
                break
        hstring = ''
        for card in h2:
            hstring += card
        for com in range(0, 9):
            seq = sequence[0+com:5+com]
            tracker = 0
            for c in seq:
                if c in hstring:
                    tracker += 1
            if tracker == 5:
                an2 = 'straight'
                stop2 = True 
                break

        kinds = []
        for card in h1:
            kinds.append(card[0])
        kinds_set = []
        for kind in kinds:
            kinds_set.append(kinds.count(kind))
        if max(kinds_set) == 3:
            an1 = 'threekind'
            stop1 = True
        elif max(kinds_set) == 2:
            if list(kinds_set).count(2) == 4:
                an1 = 'twopair'
                stop1 = True
            else:
                an1 = 'pair'
                stop1 = True
        kinds = []
        for card in h2:
            kinds.append(card[0])
        kinds_set = []
        for kind in kinds:
            kinds_set.append(kinds.count(kind))
        if max(kinds_set) == 3:
            an2 = 'threekind'
            stop2 = True
        elif max(kinds_set) == 2:
            if list(kinds_set).count(2) == 4:
                an2 = 'twopair'
                stop2 = True
            else:
                an2 = 'pair'
                stop2 = True
    
        if an1 == '':
            k = [i[0] for i in h1]
            for i in sequence[::-1]:
                if i in k:
                    an1 = i
                    break

        if an2 == '':
            k = [i[0] for i in h2]
            for i in sequence[::-1]:
                if i in k:
                    an2 = i
                    break
    
        if an2 == 'pair' and an1 == 'pair':
            kinds = []
            for card in h1:
                kinds.append(card[0])
            for kind in kinds:
                if kinds.count(kind) == 2:
                    an1 = kind
                    break 
            kinds = []
            for card in h2:
                kinds.append(card[0])
            for kind in kinds:
                if kinds.count(kind) == 2:
                    an2 = kind
                    break 
            if an1 == an2:
                an2 = 'J'

        onescore = scores[an1]
        twoscore = scores[an2]     

        if onescore>twoscore:
            one_wins += 1
        stop1 = True
        stop2 = True

print(one_wins) # 376

"""

An ugly program for an annoying problem.
Don't feel like improving it. Runs quick though.

Problem is a bit easier when you realize
you don't have to solve for every case;
royal flushes and straight flushes for example,
are so rare that you can ignore them.

"""