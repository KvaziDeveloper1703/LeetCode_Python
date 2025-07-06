'''
Roman numerals are written using the symbols I, V, X, L, C, D, and M. Each symbol has a fixed value, and numbers are formed by combining them. Usually, symbols are placed from largest to smallest, left to right.
However, if a smaller symbol comes before a larger one, it means subtraction.

Given a string S representing a Roman numeral, convert it to an integer.

Examples:
Input: "III"
Output: 3

Input: "LVIII"
Output: 58

Римские цифры записываются с использованием символов I, V, X, L, C, D и M. Каждый символ имеет фиксированное значение, а числа формируются путём их комбинации. Обычно символы записываются от большего к меньшему — слева направо.
Однако, если меньший символ стоит перед большим, это означает вычитание.

Дана строка S, представляющая римское число — преобразуйте её в целое число.

Примеры:
Вход: "III"
Выход: 3

Вход: "LVIII"
Выход: 58
'''

def roman_to_integer(S: str) -> int:
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
    previous_value = 0

    for character in reversed(S):
        current = roman[character]
        if current < previous_value:
            total -= current
        else:
            total += current
        previous_value = current

    return total