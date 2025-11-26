'''
You are given a 0-indexed integer array numbers, where numbers[i] represents the score of the i-th student. You are also given an integer k.

Choose the scores of any k students so that the difference between the highest and lowest score among those k students is minimized.

Return the minimum possible difference.

Examples:
Input: numbers = [90], k = 1
Output: 0

Input: numbers = [9,4,1,7], k = 2
Output: 2

Дан целочисленный массив numbers, индексируемый с нуля, где numbers[i] - балл i-го студента. Также дано число k.

Нужно выбрать баллы любых k студентов так, чтобы разница между максимальным и минимальным баллом среди выбранных была минимальной.

Верните минимально возможную разницу.

Примеры:
Ввод: numbers = [90], k = 1
Вывод: 0

Ввод: numbers = [9,4,1,7], k = 2
Вывод: 2
'''

from typing import List

def minimum_difference(numbers: List[int], k: int) -> int:
    if k == 1:
        return 0

    numbers.sort()
    minimum_difference = float('inf')

    for left_index in range(len(numbers) - k + 1):
        current_difference = numbers[left_index + k - 1] - numbers[left_index]
        minimum_difference = min(minimum_difference, current_difference)

    return minimum_difference