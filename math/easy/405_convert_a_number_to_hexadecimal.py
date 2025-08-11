'''
Given a 32-bit integer number, return a string representing its hexadecimal representation.
    + For negative numbers, use the two’s complement representation;
    + All letters in the output must be lowercase;
    + There should be no leading zeros, except if the number is zero;
    + You are not allowed to use any built-in library method that directly solves the problem.

Examples:
Input: number = 26
Output: "1a"

Input: number = -1
Output: "ffffffff"

Дано 32-битное целое число number. Требуется вернуть его шестнадцатеричное представление в виде строки.
    + Для отрицательных чисел используется представление в виде дополнения до двух;
    + Все буквы в ответе должны быть строчными;
    + В ответе не должно быть ведущих нулей, кроме случая, когда число равно нулю;
    + Нельзя использовать встроенные методы, которые напрямую решают эту задачу.

Примеры:
Ввод: number = 26
Вывод: "1a"

Ввод: number = -1
Вывод: "ffffffff"
'''

def to_hex(number: int) -> str:
    if number == 0:
        return "0"

    number &= 0xFFFFFFFF
    hex_characters = "0123456789abcdef"
    result_characters = []

    while number > 0:
        digit = number & 0xF
        result_characters.append(hex_characters[digit])
            number >>= 4

        return "".join(reversed(result_characters))