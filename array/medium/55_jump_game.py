'''
Given an integer array numbers. You start at the first index of the array.
Each element in the array represents the maximum number of steps you can jump forward from that position.

Return True if you can reach the last index, otherwise return False.

Examples:
Input: numbers = [2, 3, 1, 1, 4]
Output: True

Input: numbers = [3, 2, 1, 0, 4]
Output: False

Дан массив целых чисел numbers. Вы начинаете с первого индекса массива.
Каждый элемент массива указывает максимальное количество шагов, которое вы можете сделать вперёд с данной позиции.

Верните True, если можно добраться до последнего индекса массива, иначе верните False.

Примеры:
Ввод: numbers = [2, 3, 1, 1, 4]
Вывод: True

Ввод: numbers = [3, 2, 1, 0, 4]
Вывод: False
'''

from typing import List

def can_jump(numbers: List[int]) -> bool:
    max_reach = 0

    for i, jump in enumerate(numbers):
        if i > max_reach:
            return False

        max_reach = max(max_reach, i + jump)

        if max_reach >= len(numbers) - 1:
            return True

    return True