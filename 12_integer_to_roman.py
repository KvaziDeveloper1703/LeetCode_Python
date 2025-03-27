'''
Roman numerals use the symbols I, V, X, L, C, D, and M to represent numbers. To convert an integer to a Roman numeral, follow these rules:
+ Symbols are added from largest to smallest values.
+ For numbers like 4, 9, 40, 90, 400, and 900, use the subtractive form (e.g., 4 = IV, 900 = CM).
+ You can repeat symbols like I, X, C, and M up to 3 times, but never repeat V, L, or D.
+ Always convert each digit starting from the highest place value (thousands, hundreds, tens, units).

Given an integer num, convert it to its Roman numeral representation.

Examples:
Input: num = 3749
Output: "MMMDCCXLIX"

Input: num = 58
Output: "LVIII"

Input: num = 1994
Output: "MCMXCIV"
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        val_to_symbol = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]

        result = []
        for value, symbol in val_to_symbol:
            while num >= value:
                result.append(symbol)
                num -= value

        return ''.join(result)