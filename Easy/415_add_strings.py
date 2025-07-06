'''
Given two non-negative integers number_1 and number_2 represented as strings, return their sum as a string.

You must not use any built-in libraries or data types for handling large integers.
Also, do not convert the input strings directly to integers.

Examples:
Input: number_1 = "11", number_2 = "123"
Output: "134"

Input: number_1 = "456", number_2 = "77"
Output: "533"

Даны два неотрицательных целых числа, представленных в виде строк number_1 и number_2.
Верните их сумму также в виде строки.

Вы не можете использовать встроенные библиотеки или типы данных, которые работают с большими числами, и не можете напрямую преобразовывать строки в числа.

Примеры:
Вход: number_1 = "11", number_2 = "123"
Выход: "134"

Вход: number_1 = "456", number_2 = "77"
Выход: "533"
'''

def add_strings(number_1: str, number_2: str) -> str:
    i, j = len(number_1) - 1, len(number_2) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        digit_1 = ord(number_1[i]) - ord('0') if i >= 0 else 0
        digit_2 = ord(number_2[j]) - ord('0') if j >= 0 else 0
        total = digit_1 + digit_2 + carry
        carry = total // 10
        result.append(str(total % 10))
        i -= 1
        j -= 1

    return ''.join(reversed(result))