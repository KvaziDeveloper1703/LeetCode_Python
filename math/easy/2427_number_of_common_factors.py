'''
Given two positive integers a and b, return the number of common factors of a and b.

An integer x is called a common factor of a and b if x divides both a and b without a remainder.

Examples:
Input: a = 12, b = 6
Output: 4

Input: a = 25, b = 30
Output: 2

Даны два положительных целых числа a и b. Необходимо вернуть количество общих делителей чисел a и b.

Целое число x называется общим делителем чисел a и b, если x делит и a, и b без остатка.

Примеры:
Ввод: a = 12, b = 6
Вывод: 4

Ввод: a = 25, b = 30
Вывод: 2
'''

def common_factors(a: int, b: int) -> int:
    from math import gcd

    greatest_common_divisor = gcd(a, b)
    common_factors_count = 0

    for divisor in range(1, int(greatest_common_divisor ** 0.5) + 1):
        if greatest_common_divisor % divisor == 0:
            common_factors_count += 1
            if divisor != greatest_common_divisor // divisor:
                common_factors_count += 1

    return common_factors_count