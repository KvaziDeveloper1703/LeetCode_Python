'''
You are given a 0-indexed integer array numbers of length n, and two integers indexDifference and valueDifference.

Your task is to find two indices i and j (both in the range [0, n - 1]) such that:
    - |i - j| ≥ indexDifference;
    - |numbers[i] - numbers[j]| ≥ valueDifference.

If such indices exist, return an array answer = [i, j].
If no valid pair exists, return [-1, -1].
If there are multiple valid answers, you may return any of them.

Examples:
Input: numbers = [5, 1, 4, 1], indexDifference = 2, valueDifference = 4
Output: [0, 3]

Input: numbers = [2, 1], indexDifference = 0, valueDifference = 0
Output: [0, 0]

Дан целочисленный массив numbers с индексацией с нуля и длиной n, а также два целых числа indexDifference и valueDifference.

Необходимо найти два индекса i и j (оба в диапазоне от 0 до n - 1), которые удовлетворяют следующим условиям:
    - |i - j| ≥ indexDifference;
    - |numbers[i] - numbers[j]| ≥ valueDifference.

Если такие индексы существуют, верните массив answer = [i, j].
Если подходящей пары нет, верните [-1, -1].
Если существует несколько корректных вариантов, можно вернуть любой из них.

Примеры:
Ввод: numbers = [5, 1, 4, 1], indexDifference = 2, valueDifference = 4
Вывод: [0, 3]

Ввод: numbers = [2, 1], indexDifference = 0, valueDifference = 0
Вывод: [0, 0]
'''

from typing import List

def find_indices(numbers: List[int], indexDifference: int, valueDifference: int) -> List[int]:
    array_length = len(numbers)

    minimum_value = float('inf')
    maximum_value = -float('inf')

    minimum_value_index = -1
    maximum_value_index = -1

    for current_index in range(array_length):

        allowed_index = current_index - indexDifference
        if allowed_index >= 0:

            if numbers[allowed_index] < minimum_value:
                minimum_value = numbers[allowed_index]
                minimum_value_index = allowed_index

            if numbers[allowed_index] > maximum_value:
                maximum_value = numbers[allowed_index]
                maximum_value_index = allowed_index

        if (minimum_value_index != -1 and abs(numbers[current_index] - minimum_value) >= valueDifference):
                return [minimum_value_index, current_index]

        if (maximum_value_index != -1 and abs(numbers[current_index] - maximum_value) >= valueDifference):
                return [maximum_value_index, current_index]

    return [-1, -1]