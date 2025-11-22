'''
You are given a 2D integer array ranges and two integers left and right.
Each ranges[i] = [startᵢ, endᵢ] represents an inclusive interval from startᵢ to endᵢ.

Return True if every integer in the interval [left, right] is covered by at least one interval in ranges. Otherwise, return False.

An integer x is covered by an interval [startᵢ, endᵢ] if startᵢ ≤ x ≤ endᵢ.

Examples:
Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
Output: True

Input: ranges = [[1,10],[10,20]], left = 21, right = 21
Output: False

Дан двумерный массив целых чисел ranges и два числа left и right.
Каждый элемент ranges[i] = [startᵢ, endᵢ] - это включительный интервал от startᵢ до endᵢ.

Верните True, если каждое число из диапазона [left, right] покрыто хотя бы одним интервалом из ranges. В противном случае верните False.

Число x считается покрытым интервалом [startᵢ, endᵢ], если выполняется startᵢ ≤ x ≤ endᵢ.

Примеры:
Ввод: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
Вывод: True

Ввод: ranges = [[1,10],[10,20]], left = 21, right = 21
Вывод: False
'''

from typing import List

def is_covered(ranges: List[List[int]], left: int, right: int) -> bool:
    for value in range(left, right + 1):
        is_value_covered = False
        for start_value, end_value in ranges:
            if start_value <= value <= end_value:
                is_value_covered = True
                break
        if not is_value_covered:
            return False
    return True