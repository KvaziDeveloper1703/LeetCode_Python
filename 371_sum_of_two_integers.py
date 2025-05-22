'''
Given two integers a and b, return the sum of the two integers without using the + and - operators.

Examples:
Input: a = 1, b = 2
Output: 3

Input: a = 2, b = 3
Output: 5

Даны два целых числа a и b. Верните их сумму, не используя операторы + и -.

Примеры:
Ввод: a = 1, b = 2
Вывод: 3

Ввод: a = 2, b = 3
Вывод: 5
'''

def getSum(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    MAX_INT = 0x7FFFFFFF

    while b != 0:
        carry = (a & b) << 1
        a = (a ^ b) & MASK
        b = carry & MASK

    return a if a <= MAX_INT else ~(a ^ MASK)