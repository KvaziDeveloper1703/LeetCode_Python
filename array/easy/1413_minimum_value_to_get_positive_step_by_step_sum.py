'''
Given an array of integers numbers and an initial positive value startValue.

In each step, you calculate the running sum starting from startValue and adding the elements of numbers from left to right.

Return the minimum positive value of startValue such that the running sum is never less than 1 at any point.

Examples:
Input: numbers = [-3,2,-3,4,2]
Output: 5

Input: numbers = [1,2]
Output: 1

Дан массив целых чисел numbers и начальное положительное значение startValue.

На каждом шаге вычисляется промежуточная сумма, начиная с startValue и последовательно прибавляя элементы массива numbers слева направо.

Нужно вернуть минимальное положительное значение startValue, при котором промежуточная сумма никогда не становится меньше 1.

Примеры:
Ввод: numbers = [-3,2,-3,4,2]
Вывод: 5

Ввод: numbers = [1,2]
Вывод: 1
'''

from typing import List

def min_start_value(numbers: List[int]) -> int:
    running = 0
    min_prefix = 0
    for x in numbers:
        running += x
        if running < min_prefix:
            min_prefix = running
    return max(1, 1 - min_prefix)