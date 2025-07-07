"""
Given an integer n, return True if it is a power of two. Otherwise, return False.
An integer n is a power of two if there exists an integer x such that n == 2^x.

Examples:
Input: n = 1
Output: True

Input: n = 16
Output: True

Дано целое число n. Верните True, если оно является степенью двойки. В противном случае верните False.
Число n является степенью двойки, если существует целое число x, такое что n == 2^x.

Примеры:
Ввод: n = 1
Вывод: True

Ввод: n = 16
Вывод: True
"""

def is_power_of_two(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n = n // 2
    return n == 1