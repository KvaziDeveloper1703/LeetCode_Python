'''
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2³¹, 2³¹ - 1], then return 0.

Note: The environment does not allow storing 64-bit integers.

Example:
Input: x = 123
Output: 321

Дано знаковое 32-битное целое число x. Верните x, переставив его цифры в обратном порядке.
Если после разворота число выходит за пределы диапазона 32-битного знакового целого [-2³¹, 2³¹ - 1], верните 0.

Важно: нельзя использовать переменные, которые могут хранить 64-битные числа (знаковые или беззнаковые).

Пример:
Ввод: x = 123
Выход: 321
'''

def reverse(x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    sign = -1 if x < 0 else 1
    x_abs = abs(x)

    reversed_str = str(x_abs)[::-1]
    reversed_int = sign * int(reversed_str)

    if reversed_int < INT_MIN or reversed_int > INT_MAX:
        return 0

    return reversed_int