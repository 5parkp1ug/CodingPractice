"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.
"""

def int_to_roman(num: int) -> str:
    roman = ''

    while num != 0:
        if num >= 1000:
            quotient = int(num/1000)
            num = num%1000
            roman += 'M'*quotient
        elif num >= 500:
            quotient = int(num/100)
            num = num%100
            roman += 'D'+'C'*(quotient-5) if quotient != 9 else 'CM'
        elif num >= 100:
            quotient = int(num/100)
            num = num%100
            roman += 'C'*quotient if quotient != 4 else 'CD'
        elif num >= 50:
            quotient = int(num/10)
            num = num%10
            roman += 'L'+'X'*(quotient-5) if quotient != 9 else 'XC'
        elif num >= 10:
            quotient = int(num/10)
            num = num%10
            roman += 'X'*quotient if quotient != 4 else 'XL'
        else:
            if num >= 5:
                roman += 'V'+'I'*(num-5) if num != 9 else 'IX'
            else:
                roman += 'I'*num if num != 4 else 'IV'
            break
        
    return roman

if __name__ == '__main__':
    print(int_to_roman(3))
    print(int_to_roman(4))
    print(int_to_roman(9))
    print(int_to_roman(58))
    print(int_to_roman(1994))
    print(int_to_roman(60))
    print(int_to_roman(200))
    print(int_to_roman(500))
    print(int_to_roman(3000))