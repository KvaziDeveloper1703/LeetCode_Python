'''
You are given two integers, number and t.

A number x is called achievable if it can be made equal to number after applying the following operation at most t times:
    - Increase or decrease x by 1, and simultaneously increase or decrease number by 1.

Each operation changes both values by exactly 1.

Return the maximum possible value of x that is achievable.

Examples:
Input: number = 4, t = 1
Output: 6

Input: number = 3, t = 2
Output: 7

Даны два целых числа number и t.

Число x называется достижимым, если его можно сделать равным number, применив следующую операцию не более t раз:
    - увеличить или уменьшить x на 1 и одновременно увеличить или уменьшить number на 1.

Каждая операция изменяет оба числа ровно на 1.

Вернуть максимально возможное значение числа x, которое является достижимым.

Примеры:
Ввод: number = 4, t = 1
Вывод: 6

Ввод: number = 3, t = 2
Вывод: 7
'''

def the_maximum_achievable_x(number: int, t: int) -> int:
    return number + 2 * t