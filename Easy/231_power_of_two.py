"""
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two if there exists an integer x such that n == 2^x.

Examples:
Input: n = 1
Output: true

Input: n = 16
Output: true

Дано целое число n. Верните true, если оно является степенью двойки. В противном случае верните false.
Число n является степенью двойки, если существует целое число x, такое что n == 2^x.

Примеры:
Ввод: n = 1
Вывод: true

Ввод: n = 16
Вывод: true
"""

def is_power_of_two(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n = n // 2
    return n == 1