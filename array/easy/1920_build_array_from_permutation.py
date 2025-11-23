'''
You are given a zero-based permutation numbers.
Build an array answer of the same length, where for every index i: answer[i]=numbers[numbers[i]].

Return the resulting array answer.

A zero-based permutation is an array of distinct integers from 0 to numbers.length - 1.

Examples:
Input: numbers = [0, 2, 1, 5, 3, 4]
Output: [0, 1, 2, 4, 5, 3]

Input: numbers = [5, 0, 1, 2, 3, 4]
Output: [4, 5, 0, 1, 2, 3]

Дана перестановка numbers с нумерацией с нуля.
Нужно построить массив answer той же длины, где для каждого индекса i: answer[i]=numbers[numbers[i]].

Верните полученный массив answer.

Перестановка с нумерацией с нуля - это массив из различных целых чисел от 0 до numbers.length - 1 включительно.

Примеры:
Ввод: numbers = [0, 2, 1, 5, 3, 4]
Вывод: [0, 1, 2, 4, 5, 3]

Ввод: numbers = [5, 0, 1, 2, 3, 4]
Вывод: [4, 5, 0, 1, 2, 3]
'''

from typing import List

def build_array(numbers: List[int]) -> List[int]:
    length = len(numbers)
    result = [0] * length

    for i in range(length):
        index = numbers[i]
        value = numbers[index]
        result[i] = value

    return result