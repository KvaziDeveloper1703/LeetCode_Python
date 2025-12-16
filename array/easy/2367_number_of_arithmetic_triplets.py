'''
You are given a 0-indexed, strictly increasing array of integers numbers and a positive integer diff.

A triplet (i, j, k) is called an arithmetic triplet if the following conditions are satisfied:
    - i < j < k;
    - numbers[j] - numbers[i] = diff;
    - numbers[k] - numbers[j] = diff.

Return the number of unique arithmetic triplets in the array numbers.

Examples:
Input: numbers = [0, 1, 4, 6, 7, 10], diff = 3
Output: 2

Input: numbers = [4, 5, 6, 7, 8, 9], diff = 2
Output: 2

Вам дан 0-индексированный, строго возрастающий массив целых чисел numbers и положительное целое число diff.

Тройка индексов (i, j, k) называется арифметической тройкой, если выполняются следующие условия:
    - i < j < k;
    - numbers[j] - numbers[i] = diff;
    - numbers[k] - numbers[j] = diff.

Необходимо определить количество уникальных арифметических троек в массиве numbers.

Примеры:
Ввод: numbers = [0, 1, 4, 6, 7, 10], diff = 3
Вывод: 2

Ввод: numbers = [4, 5, 6, 7, 8, 9], diff = 2
Вывод: 2
'''

from typing import List

def arithmetic_triplets(numbers: List[int], diff: int) -> int:
    numbers_set = set(numbers)
    count = 0

    for value in numbers:
        if value + diff in numbers_set and value + 2 * diff in numbers_set:
            count += 1

    return count