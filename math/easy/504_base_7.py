'''
Given an integer number, return a string representing its base 7 representation.

Examples:
Input: number = 100
Output: "202"

Input: number = -7
Output: "-10"

Дано целое число number. Верните строку, представляющую его запись в семеричной системе счисления (с основанием 7).

Примеры:
Ввод: number = 100
Вывод: "202"

Ввод: number = -7
Вывод: "-10"
'''

def convert_to_base_7(number: int) -> str:
    if number == 0:
        return "0"

    negative = number < 0
    number = abs(number)
    result = ""

    while number > 0:
        result = str(number % 7) + result
        number //= 7

    return "-" + result if negative else result