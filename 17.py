one_translation_dict = {
    '1': ['one', 'ten'],
    '2': ['two', 'twenty'],
    '3': ['three', 'thirty'],
    '4': ['four', 'forty'],
    '5': ['five', 'fifty'],
    '6': ['six', 'sixty'],
    '7': ['seven', 'seventy'],
    '8': ['eight', 'eighty'],
    '9': ['nine', 'ninety']
}

two_translation_dict = {
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
}

def parse(number):
    str1 = str(number)
    if number == 0:
        return 4
    if number == 1000:
        return 11
    if len(str1) > 1: 
        if number < 20: 
            return len(two_translation_dict[str1])
        else: 
            hunds = 0
            if number > 99: 
                if number % 100 == 0:
                    return len(one_translation_dict[str1[0]][0]) + len('hundred')
                else:
                    hunds = len(one_translation_dict[str1[0]][0]) + len('hundred') + len('and')
            tens_places = str1[-2:]
            tens = 0
            if tens_places[0] == '0':
                return hunds + len(one_translation_dict[tens_places[1]][0])
            else:
                if int(tens_places) % 10 == 0:
                    tens = len(one_translation_dict[tens_places[0]][1]) 
                else:
                    if int(tens_places) < 20: 
                        tens = len(two_translation_dict[tens_places])   

                    else:
                        tens = len(one_translation_dict[str1[-2]][1]) + len(one_translation_dict[str1[-1]][0])

                return tens + hunds
    else:
        return len(one_translation_dict[str1][0])

sum1 = 0
for i in range(1,1001):
    sum1 += parse(i)

print(sum1) # 21124