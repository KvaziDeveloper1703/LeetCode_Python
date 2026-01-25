'''
You are given an array numbers consisting of n prime integers.
You need to build an array answer of length n such that for every index i: the bitwise OR of answer[i] and answer[i] + 1 is equal to numbers[i].
So for each position i, you must find the smallest possible value answer[i] such that: answer[i] OR (answer[i] + 1) gives numbers[i].
If it is not possible to find such a value for some index i, then set: answer[i] = -1.
Return the resulting array answer.

Examples:
Input: numbers = [2, 3, 5, 7]
Output: [-1, 1, 4, 3]

Input: numbers = [11, 13, 31]
Output: [9, 12, 15]

Вам дан массив numbers, состоящий из n простых чисел.
Нужно построить массив answer длины n так, чтобы для каждого индекса i выполнялось условие: побитовое OR между числом answer[i] и числом answer[i] + 1 должно быть равно numbers[i].
То есть для каждой позиции i нужно найти минимально возможное значение answer[i], при котором: answer[i] OR (answer[i] + 1) даёт numbers[i].
Если для какого-то индекса i подобрать такое значение невозможно, тогда нужно записать: answer[i] = -1.
Верните получившийся массив answer.

Примеры:
Ввод: numbers = [2, 3, 5, 7]
Вывод: [-1, 1, 4, 3]

Ввод: numbers = [11, 13, 31]
Вывод: [9, 12, 15]
'''

from typing import List

def min_bitwise_array(numbers: List[int]) -> List[int]:
    answer = []

    for value in numbers:
        if value % 2 == 0:
            answer.append(-1)
            continue

        trailing_ones = 0
        temp_value = value
        while temp_value & 1 == 1:
            trailing_ones += 1
            temp_value >>= 1

        bit_to_clear = 1 << (trailing_ones - 1)
        minimal_value = value - bit_to_clear
        answer.append(minimal_value)

    return answer