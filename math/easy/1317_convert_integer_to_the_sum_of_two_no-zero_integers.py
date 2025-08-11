'''
A No-Zero integer is a positive integer that does not contain any zero digits in its decimal representation.

Given an integer n, return a list of two positive integers [a, b] such that:
    + Both a and b are No-Zero integers;
    + a + b = n.

It is guaranteed that at least one valid solution exists. If multiple solutions exist, you can return any of them.

Examples:
Input: n = 2
Output: [1, 1]

Input: n = 11
Output: [2, 9]

Безноликовое число — это положительное целое число, не содержащее ни одной цифры 0 в десятичной записи.

Дано целое число n. Необходимо вернуть список из двух положительных безноликовых чисел [a, b], таких что:
    + И a, и b являются безноликовыми числами;
    + a + b = n.

Гарантируется, что хотя бы одно решение всегда существует. Если существует несколько решений — можно вернуть любое из них.

Примеры:
Ввод: n = 2
Вывод: [1, 1]

Ввод: n = 11
Вывод: [2, 9]
'''

from typing import List

def get_no_zero_integers(n: int) -> List[int]:
    def has_zero(x: int) -> bool:
        return '0' in str(x)

    for a in range(1, n):
        b = n - a
        if not has_zero(a) and not has_zero(b):
            return [a, b]