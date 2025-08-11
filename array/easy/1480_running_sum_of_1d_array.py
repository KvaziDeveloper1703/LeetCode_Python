"""
Given an array of integers numbers, return the running sum of the array.
The running sum at index i is defined as the sum of all elements from index 0 to i: running_sum[i] = numbers[0] + numbers[1] + ... + numbers[i]

Examples:
Input: numbers = [1, 2, 3, 4]
Output: [1, 3, 6, 10]

Input: numbers = [1, 1, 1, 1, 1]
Output: [1, 2, 3, 4, 5]

Дан массив целых чисел numbers. Необходимо вернуть префиксную сумму этого массива.
Префиксная сумма на индексе i — это сумма всех элементов от индекса 0 до i: running_sum[i] = numbers[0] + numbers[1] + ... + numbers[i]

Примеры:
Ввод: numbers = [1, 2, 3, 4]
Вывод: [1, 3, 6, 10]

Ввод: numbers = [1, 1, 1, 1, 1]
Вывод: [1, 2, 3, 4, 5]
"""

from typing import List

def running_sum(numbers: List[int]) -> List[int]:
    result = []
    current_sum = 0

    for number in numbers:
        current_sum += number
        result.append(current_sum)

    return result