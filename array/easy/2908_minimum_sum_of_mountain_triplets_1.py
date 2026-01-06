'''
You are given a 0-indexed integer array numbers.

A triplet of indices (i, j, k) is called a mountain if the following conditions are satisfied:
    - i < j < k;
    - numbers[i] < numbers[j] and numbers[k] < numbers[j].

Your task is to return the minimum possible sum of a mountain triplet: numbers[i] + numbers[j] + numbers[k].

If no such mountain triplet exists, return -1.

Examples:
Input: numbers = [8, 6, 1, 5, 3]
Output: 9

Input: numbers = [5, 4, 8, 7, 10, 2]
Output: 13

Дан целочисленный массив numbers с индексацией с нуля.

Тройка индексов (i, j, k) называется горной (mountain), если выполняются следующие условия:
    - i < j < k;
    - numbers[i] < numbers[j] и numbers[k] < numbers[j].

Необходимо найти минимально возможную сумму элементов горной тройки: numbers[i] + numbers[j] + numbers[k].

Если ни одной горной тройки не существует, верните -1.

Примеры:
Ввод: numbers = [8, 6, 1, 5, 3]
Вывод: 9

Ввод: numbers = [5, 4, 8, 7, 10, 2]
Вывод: 13
'''

from typing import List

def minimum_sum(numbers: List[int]) -> int:
    array_length = len(numbers)

    left_minimum = [float('inf')] * array_length
    right_minimum = [float('inf')] * array_length

    left_minimum[0] = numbers[0]
    for index in range(1, array_length):
        left_minimum[index] = min(left_minimum[index - 1], numbers[index])

    right_minimum[array_length - 1] = numbers[array_length - 1]
    for index in range(array_length - 2, -1, -1):
        right_minimum[index] = min(right_minimum[index + 1], numbers[index])

    minimum_sum = float('inf')

    for middle_index in range(1, array_length - 1):
        if (left_minimum[middle_index - 1] < numbers[middle_index] and right_minimum[middle_index + 1] < numbers[middle_index]):
                current_sum = (left_minimum[middle_index - 1] + numbers[middle_index] + right_minimum[middle_index + 1])
                minimum_sum = min(minimum_sum, current_sum)

    return minimum_sum if minimum_sum != float('inf') else -1