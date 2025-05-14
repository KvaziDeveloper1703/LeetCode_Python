'''
Given an integer n, count the total number of digit '1' that appears in all non-negative integers less than or equal to n.

Examples:
Input: n = 13
Output: 6

Input: n = 0
Output: 0

Дано целое число n. Посчитайте общее количество цифр '1', которые встречаются во всех неотрицательных числах от 0 до n включительно.

Примеры:
Ввод: n = 13
Вывод: 6

Ввод: n = 0
Вывод: 0
'''

def count_digit_one(n: int) -> int:
    count = 0
    factor = 1

    while factor <= n:
        higher = n // (factor * 10)
        current = (n // factor) % 10
        lower = n % factor

        if current == 0:
            count += higher * factor
        elif current == 1:
            count += higher * factor + lower + 1
        else:
            count += (higher + 1) * factor

        factor *= 10

    return count