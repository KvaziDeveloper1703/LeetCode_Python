'''
You are given a positive integer n.

Your task is to find the smallest integer x such that: x ≥ n, and the binary representation of x consists only of set bits (that is, all bits are 1).

Return the value of x.

Examples:
Input: n = 5
Output: 7

Input: n = 10
Output: 15

Дано положительное целое число n.

Требуется найти наименьшее целое число x, такое что: x ≥ n, и двоичное представление числа x состоит только из установленных битов (то есть все биты равны 1).

Верните значение x.

Примеры:
Ввод: n = 5
Вывод: 7

Ввод: n = 10
Вывод: 15
'''

def smallest_number(n: int) -> int:
    bit_length = n.bit_length()
    candidate = (1 << bit_length) - 1

    if candidate >= n:
        return candidate
    else:
        return (1 << (bit_length + 1)) - 1