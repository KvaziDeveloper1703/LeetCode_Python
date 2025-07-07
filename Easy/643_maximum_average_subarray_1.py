'''
You are given an integer array numbers containing n elements, and an integer k.
Find a contiguous subarray of length exactly k that has the maximum average value, and return this value.
Any answer with a calculation error less than 10^-5 will be accepted.

Examples:
Input: numbers = [1,12,-5,-6,50,3], k = 4
Output: 12.75000

Input: numbers = [5], k = 1
Output: 5.00000

Дан массив целых чисел numbers, состоящий из n элементов, и целое число k.
Необходимо найти непрерывную подпоследовательность длиной ровно k, у которой среднее значение максимально, и вернуть это значение.
Результат считается правильным, если ошибка вычислений не превышает 10^-5.

Примеры:
Ввод: numbers = [1,12,-5,-6,50,3], k = 4
Вывод: 12.75000

Ввод: numbers = [5], k = 1
Вывод: 5.00000
'''

from typing import List

def find_max_average(numbers: List[int], k: int) -> float:
    window_sum = sum(numbers[:k])
    max_sum = window_sum
        
    for i in range(k, len(numbers)):
        window_sum += numbers[i] - numbers[i - k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum / k