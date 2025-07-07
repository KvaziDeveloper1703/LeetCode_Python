'''
An ugly number is a positive integer whose only prime factors are 2, 3, and 5.
Given an integer n, return True if n is an ugly number, and False otherwise.

Examples:
Input: n = 6
Output: True

Input: n = 1
Output: True

"Уродливое число" — это положительное целое число, у которого нет простых делителей, кроме 2, 3 и 5.
Дано целое число n. Верните True, если n — уродливое число, и False в противном случае.

Примеры:
Ввод: n = 6
Вывод: True

Ввод: n = 1
Вывод: True
'''

def is_ugly(n: int) -> bool:
    if n <= 0:
        return False
    for p in [2, 3, 5]:
        while n % p == 0:
            n //= p
    return n == 1