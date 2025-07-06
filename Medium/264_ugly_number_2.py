'''
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the n-th ugly number.

Examples:
Input: n = 10
Output: 12

Input: n = 1
Output: 1

"Уродливое число" — это положительное целое число, простые делители которого ограничены только числами 2, 3 и 5.
Дано целое число n. Верните n-е по счёту уродливое число.

Примеры:
Вход: n = 10
Выход: 12

Вход: n = 1
Выход: 1
'''

def nth_ugly_number(self, n: int) -> int:
    ugly = [1]
    i2 = i3 = i5 = 0

    while len(ugly) < n:
        next_2, next_3, next_5 = ugly[i2]*2, ugly[i3]*3, ugly[i5]*5
        next_ugly = min(next_2, next_3, next_5)
        ugly.append(next_ugly)

        if next_ugly == next_2:
            i2 += 1
        if next_ugly == next_3:
            i3 += 1
        if next_ugly == next_5:
            i5 += 1

    return ugly[-1]