'''
Given an array of integers numbers.

Return the number of good pairs.

A pair of indices (i, j) is called good if: numbers[i] == numbers[j], and i < j

Examples:
Input: numbers = [1,2,3,1,1,3]
Output: 4

Input: numbers = [1,1,1,1]
Output: 6

Дан массив целых чисел numbers.

Нужно вернуть количество хороших пар.

Пара индексов (i, j) называется хорошей, если выполняются условия: numbers[i] == numbers[j], and i < j

Примеры:
Ввод: numbers = [1,2,3,1,1,3]
Вывод: 4

Ввод: numbers = [1,1,1,1]
Вывод: 6
'''

from typing import List

def number_of_identical_pairs(numbers: List[int]) -> int:
    seen = {}
    answer = 0
    for x in numbers:
        answer += seen.get(x, 0)
        seen[x] = seen.get(x, 0) + 1
    return answer