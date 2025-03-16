import math
def generate_fractions(n):
    fractions = []
    for numerator in range(1, n):
        for denominator in range(numerator + 1, n + 1):  
            gcd = math.gcd(numerator,denominator)
            if [numerator/gcd, denominator/gcd] not in fractions:
                fractions.append([numerator/gcd, denominator/gcd])
            
    return list(fractions)
