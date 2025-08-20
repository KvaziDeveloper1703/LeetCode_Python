'''
Given two non-negative integers low and high.

Return the count of odd numbers between low and high.

Examples:
Input: low = 3, high = 7
Output: 3

Input: low = 8, high = 10
Output: 1

Даны два неотрицательных целых числа low и high.

Нужно вернуть количество нечётных чисел в диапазоне от low до high включительно.

Примеры:
Ввод: low = 3, high = 7
Вывод: 3

Ввод: low = 8, high = 10
Вывод: 1
'''

def count_odds(low: int, high: int) -> int:
    count = 0
    for number in range(low, high + 1):
        if number % 2 == 1:
            count += 1
    return count