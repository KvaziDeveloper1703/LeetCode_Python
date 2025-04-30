'''
You are given two integers, dividend and divisor. Your task is to perform integer division between them without using the multiplication (*), division (/), or modulo (%) operators. 
The result of the division must be truncated toward zero, which means any fractional part must be discarded. For example, dividing 8.345 would result in 8, and dividing -2.7335 would result in -2.
The function should return the quotient after dividing dividend by divisor. However, if the result of the division exceeds the range of a 32-bit signed integer, 
which is from -2³¹ to 2³¹ − 1, then you must return 2147483647 if the result is too large, or -2147483648 if it is too small.

Examples:
Input: dividend = 10, divisor = 3
Output: 3

Input: dividend = 7, divisor = -3
Output: -2

Даны два целых числа: dividend (делимое) и divisor (делитель). Необходимо выполнить деление этих чисел без использования операторов умножения (*), деления (/) и остатка от деления (%). 
Результат деления должен быть усечён в сторону нуля, то есть дробная часть должна быть отброшена. Например, при делении 8.345 результатом должно быть 8, а при делении -2.7335 — результатом должно быть -2.
Функция должна вернуть частное от деления dividend на divisor. Если результат выходит за пределы допустимого диапазона 32-битного целого числа со знаком 
(от -2³¹ до 2³¹ − 1, то есть от -2147483648 до 2147483647), то необходимо вернуть 2147483647, если результат превышает предел, или -2147483648, если он меньше допустимого значения.

Примеры:
Ввод: dividend = 10, divisor = 3
Вывод: 3

Ввод: dividend = 7, divisor = -3
Вывод: -2
'''

def divide(dividend: int, divisor: int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    negative = (dividend < 0) != (divisor < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    quotient = 0

    while dividend >= divisor:
        temporary = divisor
        multiple = 1
        while dividend >= (temporary << 1):
            temporary <<= 1
            multiple <<= 1
        dividend -= temporary
        quotient += multiple

    return -quotient if negative else quotient