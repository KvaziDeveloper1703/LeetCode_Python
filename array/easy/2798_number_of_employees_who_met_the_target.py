'''
There are n employees in a company, numbered from 0 to n - 1.

Each employee i has worked hours[i] hours.

The company requires every employee to work for at least target hours.

You are given:
    - a 0-indexed array of non-negative integers hours of length n, and
    - a non-negative integer target.

Return the number of employees who worked at least target hours.

Examples:
Input: hours = [0, 1, 2, 3, 4], target = 2
Output: 3

Input: hours = [5, 1, 4, 2, 2], target = 6
Output: 0

В компании работает n сотрудников, пронумерованных от 0 до n - 1.

Каждый сотрудник i отработал hours[i] часов.

Компания требует, чтобы каждый сотрудник отработал не менее target часов.

Вам даны:
    - 0-индексированный массив неотрицательных целых чисел hours длины n, и
    - неотрицательное целое число target.

Необходимо вернуть количество сотрудников, которые отработали как минимум target часов.

Примеры:
Ввод: hours = [0, 1, 2, 3, 4], target = 2
Вывод: 3

Ввод: hours = [5, 1, 4, 2, 2], target = 6
Вывод: 0
'''

from typing import List

def number_of_employees_who_met_target(hours: List[int], target: int) -> int:
    count = 0

    for h in hours:
        if h >= target:
            count += 1

    return count