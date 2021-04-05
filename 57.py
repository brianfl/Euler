from decimal import *
numerator = Decimal(1393)
denominator = Decimal(985)
cumulator = 1

for i in range(0, 992):
    
    numerator = round(numerator * Decimal((round(2**.5 + 1, 6))))
    denominator = round(denominator * Decimal((round(2**.5 + 1, 6))))
    if len(str(numerator)) > len(str(denominator)):
        cumulator += 1

print(cumulator) # 153

"""
Using the decimal library to get around infinite float errors in Python...
"""
