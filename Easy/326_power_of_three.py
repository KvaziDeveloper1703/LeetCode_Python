'''
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three if there exists an integer x such that:
n == 3ˣ

Examples:
Input: n = 27
Output: true

Input: n = 0
Output: false

Дано целое число n. Верните true, если n является степенью тройки, и false — в противном случае.
Целое число n считается степенью тройки, если существует такое целое число x, что:
n == 3ˣ

Примеры:
Вход: n = 27
Выход: true

Вход: n = 0
Выход: false
'''

def is_power_of_three(self, n: int) -> bool:
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1