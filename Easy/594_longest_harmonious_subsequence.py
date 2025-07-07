'''
We say that an array is harmonious if the difference between its maximum and minimum element is exactly 1.
Given an integer array numbers, return the length of the longest harmonious subsequence you can find among all its possible subsequences.
A subsequence is formed by deleting zero or more elements without changing the order of the remaining elements.

Examples:
Input: numbers = [1,3,2,2,5,2,3,7]
Output: 5

Input: numbers = [1,2,3,4]
Output: 2

Назовём массив гармоничным, если разница между его максимальным и минимальным элементом ровно 1.
Дан целочисленный массив numbers. Нужно вернуть длину самой длинной гармоничной подпоследовательности, которую можно получить из этого массива.
Подпоследовательность образуется удалением нуля или более элементов из массива без изменения порядка оставшихся элементов.

Примеры:
Ввод: numbers = [1,3,2,2,5,2,3,7]
Вывод: 5

Ввод: numbers = [1,2,3,4]
Вывод: 2
'''

from collections import Counter
from typing import List

def find_LHS(numbers: List[int]) -> int:
    count = Counter(numbers)
    max_length = 0
    for number in count:
        if number + 1 in count:
            max_length = max(max_length, count[number] + count[number + 1])
    return max_length