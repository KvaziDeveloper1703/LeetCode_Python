'''
Given an integer array numbers consisting of 2n integers, your task is to group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized.
Return the maximum possible sum.

Examples:
Input: numbers = [1,4,3,2]
Output: 4

Input: numbers = [6,2,6,5,1,2]
Output: 9

Дан целочисленный массив numbers, состоящий из 2n элементов. Необходимо сгруппировать эти числа в n пар (a1, b1), (a2, b2), ..., (an, bn) так, чтобы сумма min(ai, bi) по всем i была максимально возможной.
Нужно вернуть эту максимальную сумму.

Примеры:
Ввод: numbers = [1,4,3,2]
Вывод: 4

Ввод: numbers = [6,2,6,5,1,2]
Вывод: 9
'''

from typing import List

def array_pair_sum(numbers: List[int]) -> int:
    numbers.sort()
    total = 0

    for i in range(0, len(numbers), 2):
        total += numbers[i]

    return total