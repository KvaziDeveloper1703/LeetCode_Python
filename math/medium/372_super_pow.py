'''
Your task is to calculate base**exponent_digits mod 1337, where:
    + base is a positive integer;
    + exponent_digits is a very large positive integer, represented as an array of digits.

Examples:
Input: base = 2, exponent_digits = [3]
Output: 8

Input: base = 2, exponent_digits = [1, 0]
Output: 1024

Ваша задача — вычислить base**exponent_digits mod 1337, где:
    + base — положительное целое число;
    + exponent_digits — очень большое положительное число, заданное в виде массива цифр.

Примеры:
Ввод: base = 2, exponent_digits = [3]
Вывод: 8

Ввод: base = 2, exponent_digits = [1, 0]
Вывод: 1024
'''

def super_pow(base: int, exponent_digits: list[int]) -> int:
    def modular_exponentiation(base_value: int, exponent_value: int) -> int:
        base_value %= 1337
        result = 1

        for _ in range(exponent_value):
            result = (result * base_value) % 1337
        return result

    if not exponent_digits:
        return 1

    current_exponent_digit = exponent_digits.pop()
    partial_result = super_pow(base, exponent_digits)
    powered_partial_result = modular_exponentiation(partial_result, 10)
    current_digit_power = modular_exponentiation(base, current_exponent_digit)

    return (powered_partial_result * current_digit_power) % 1337