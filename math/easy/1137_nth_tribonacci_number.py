'''
The Tribonacci sequence is defined as follows:
    - T0 = 0;
    - T1 = 1;
    - T2 = 1;
    - For n >= 0: T(n+3) = T(n) + T(n+1) + T(n+2).

Given an integer n, return the value of Tn.

Examples:
Input: n = 4
Output: 4

Input: n = 25
Output: 1389537

Последовательность Трибоначчи определяется следующим образом:
    - T0 = 0;
    - T1 = 1;
    - T2 = 1;
    - For n >= 0: T(n+3) = T(n) + T(n+1) + T(n+2).

Дано число n. Необходимо вернуть значение Tn.

Примеры:
Ввод: n = 4
Вывод: 4

Ввод: n = 25
Вывод: 1389537
'''

def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    a, b, c = 0, 1, 1

    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c

    return c