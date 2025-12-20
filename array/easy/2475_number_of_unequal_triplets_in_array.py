'''
You are given a 0-indexed array numbers consisting of positive integers.

Your task is to determine how many triplets of indices (i, j, k) satisfy the following conditions:
    - 0 ≤ i < j < k < numbers.length;
    - The elements numbers[i], numbers[j], and numbers[k] are pairwise distinct, meaning:
        - numbers[i] ≠ numbers[j];
        - numbers[i] ≠ numbers[k];
        - numbers[j] ≠ numbers[k].

Return the number of such triplets.

Examples:
Input:numbers = [4, 4, 2, 4, 3]
Output: 3

Input: numbers = [1, 1, 1, 1, 1]
Output: 0

Дан 0-индексированный массив numbers, состоящий из положительных целых чисел.

Необходимо найти количество троек индексов (i, j, k), которые удовлетворяют следующим условиям:
    - 0 ≤ i < j < k < numbers.length;
    - Элементы numbers[i], numbers[j] и numbers[k] попарно различны, то есть:
        - numbers[i] ≠ numbers[j];
        - numbers[i] ≠ numbers[k];
        - numbers[j] ≠ numbers[k].

Верните количество таких троек.

Примеры:
Ввод: numbers = [4, 4, 2, 4, 3]
Вывод: 3

Ввод: numbers = [1, 1, 1, 1, 1]
Вывод: 0
'''

from typing import List
from collections import Counter

def unequal_triplets(numbers: List[int]) -> int:
    frequency = Counter(numbers)
    total_elements = len(numbers)

    result = 0
    processed = 0

    for count in frequency.values():
        remaining = total_elements - processed - count
        result += processed * count * remaining
        processed += count

    return result