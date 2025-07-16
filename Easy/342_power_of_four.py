'''
Given an integer n, return True if it is a power of four. Otherwise, return False.
An integer n is a power of four if there exists an integer x such that: n == 4^x.

Examples:
Input: n = 16
Output: True

Input: n = 5
Output: False

Дано целое число n. Верни True, если оно является степенью числа четыре. Иначе верни False.
Целое число n является степенью числа четыре, если существует целое число x, такое что: n == 4^x.

Примеры:
Ввод: n = 16
Вывод: True

Ввод: n = 5
Вывод: False
'''

def is_power_of_four(n: int) -> bool:
    if n <= 0:
        return False
    while n % 4 == 0:
        n //= 4
    return n == 1