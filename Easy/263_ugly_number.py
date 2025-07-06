'''
An ugly number is a positive integer whose only prime factors are 2, 3, and 5.
Given an integer n, return true if n is an ugly number, and false otherwise.

Examples:
Input: n = 6
Output: true

Input: n = 1
Output: true

"Уродливое число" — это положительное целое число, у которого нет простых делителей, кроме 2, 3 и 5.
Дано целое число n. Верните true, если n — уродливое число, и false в противном случае.

Примеры:
Вход: n = 6
Выход: true

Вход: n = 1
Выход: true
'''

def is_ugly(self, n: int) -> bool:
    if n <= 0:
        return False
    for p in [2, 3, 5]:
        while n % p == 0:
            n //= p
    return n == 1