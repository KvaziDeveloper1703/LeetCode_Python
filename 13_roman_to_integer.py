'''
Roman numerals are written using the symbols I, V, X, L, C, D, and M. Each symbol has a fixed value, and numbers are formed by combining them. Usually, symbols are placed from largest to smallest, left to right.
However, if a smaller symbol comes before a larger one, it means subtraction (e.g., IV = 4, IX = 9).

Given a string s representing a Roman numeral, convert it to an integer.

Examples:
Input: "III" → Output: 3
Input: "LVIII" → Output: 58
Input: "MCMXCIV" → Output: 1994
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        for char in reversed(s):
            current = roman[char]
            if current < prev_value:
                total -= current
            else:
                total += current
            prev_value = current

        return total