'''
You are given an integer n. Return True if n has exactly three positive divisors; otherwise, return False.

A number m is a divisor of n if there exists an integer k such that n = k · m.

Examples:
Input: n = 2
Output: False

Input: n = 4
Output: True

Дано целое число n. Верните True, если у числа n ровно три положительных делителя; иначе верните False.

Число m является делителем n, если существует целое число k, такое что n = k · m.

Примеры:
Ввод: n = 2
Вывод: False

Ввод: n = 4
Вывод: True
'''

def is_three(n: int) -> bool:
    divisor_count = 0

    for number in range(1, int(n ** 0.5) + 1):
        if n % number == 0:
            divisor_count += 1
            if number != n // number:
                divisor_count += 1

        if divisor_count > 3:
            return False

    return divisor_count == 3