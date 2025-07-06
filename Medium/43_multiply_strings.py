'''
Given two non-negative integers number_1 and number_2 represented as strings, return the product of number_1 and number_2, also represented as a string.
You must not use any built-in BigInteger library or convert the inputs to integers directly.

Examples:
Input: number_1 = "2", number_2 = "3"
Output: "6"

Input: number_1 = "123", number_2 = "456"
Output: "56088"

Даны два неотрицательных целых числа number_1 и number_2, представленные в виде строк. Верните произведение этих чисел, также в виде строки.
Нельзя использовать встроенные библиотеки для работы с большими числами или напрямую преобразовывать строки в числа.

Примеры:
Ввод: number_1 = "2", number_2 = "3"
Вывод: "6"

Ввод: number_1 = "123", number_2 = "456"
Вывод: "56088"
'''

def multiply(first_number: str, second_number: str) -> str:
    if first_number == "0" or second_number == "0":
        return "0"

    length_first = len(first_number)
    length_second = len(second_number)
    result_digits = [0] * (length_first + length_second)

    for index_first in range(length_first - 1, -1, -1):
        for index_second in range(length_second - 1, -1, -1):
            digit_first = int(first_number[index_first])
            digit_second = int(second_number[index_second])
            product = digit_first * digit_second
            position_leading = index_first + index_second
            position_trailing = index_first + index_second + 1

            total = product + result_digits[position_trailing]
            result_digits[position_trailing] = total % 10
            result_digits[position_leading] += total // 10

    result_string = ''.join(map(str, result_digits)).lstrip('0')
    return result_string or "0"