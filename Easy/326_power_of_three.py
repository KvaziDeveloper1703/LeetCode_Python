'''
Given an integer n, return True if it is a power of three. Otherwise, return False.
An integer n is a power of three if there exists an integer x such that: n == 3ˣ

Examples:
Input: n = 27
Output: True

Input: n = 0
Output: False

Дано целое число n. Верните True, если n является степенью тройки, и False — в противном случае.
Целое число n считается степенью тройки, если существует такое целое число x, что: n == 3ˣ

Примеры:
Вход: n = 27
Выход: True

Вход: n = 0
Выход: False
'''

def is_power_of_three(n: int) -> bool:
    if n <= 0:
        return False

    while n % 3 == 0:
        n //= 3

    return n == 1