'''
Given a positive integer n. The complement of an integer is the number you get by flipping all the bits in its binary representation:
    + Replace every 1 with 0, and every 0 with 1.

Return the complement of n.

Examples:
Input: n = 5
Output: 2

Input: n = 7
Output: 0

Вам дано положительное целое число n. Дополнение числа — это число, полученное путём инвертирования всех битов в его двоичном представлении:
    + Каждый 1 заменяется на 0, а каждый 0 — на 1.

Верните дополнение числа n.

Примеры:
Ввод: n = 5
Вывод: 2

Ввод: n = 7
Вывод: 0
'''

def bitwise_complement(n: int) -> int:
    if n == 0:
        return 1

    bit_length = n.bit_length()
    mask = (1 << bit_length) - 1

    return n ^ mask