'''
Implement the my_atoi function, which converts a string to a 32-bit signed integer.

Algorithm:
    + Whitespace: Ignore any leading whitespace " ";
    + Signedness: Check for a '+' or '-' sign; default to positive if none;
    + Conversion: Read in digits until a non-digit character or end of string is reached;
    + Rounding: Clamp the result to fit in the 32-bit signed integer range: [-2³¹, 2³¹ - 1].

Example:
Input: S = "42"
Output: 42

Реализуйте функцию my_atoi(), которая преобразует строку в 32-битное знаковое целое число.

Алгоритм:
    + Пробелы: Пропустить все начальные пробелы " ";
    + Знак: Определить знак числа: '-' или '+'. Если знака нет, предполагается положительное число;
    + Конвертация: Читать цифры до первого нецифрового символа или конца строки;
    + Ограничение: Если число выходит за диапазон [-2³¹, 2³¹ - 1], обрезать его до границ.

Пример:
Ввод: S = "42"
Вывод: 42
'''

def my_atoi(S: str) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    i = 0
    n = len(S)

    while i < n and S[i] == ' ':
        i += 1

    sign = 1

    if i < n and (S[i] == '-' or S[i] == '+'):
        if S[i] == '-':
            sign = -1
        i += 1

    result = 0

    while i < n and S[i].isdigit():
        digit = int(S[i])
        if result > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        result = result * 10 + digit
        i += 1

    return sign * result