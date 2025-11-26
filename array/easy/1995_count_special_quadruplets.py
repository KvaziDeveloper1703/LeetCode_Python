'''
You are given a 0-indexed integer array numbers.
Return the number of distinct quadruplets such that:
    - numbers[a] + numbers[b] + numbers[c] == numbers[d], and
    - a < b < c < d.

Examples:
Input: numbers = [1,2,3,6]
Output: 1

Input: numbers = [3,3,6,4,5]
Output: 0

Дан целочисленный массив numbers, индексируемый с нуля.
Нужно вернуть количество различных четверок индексов, для которых:
    - numbers[a] + numbers[b] + numbers[c] == numbers[d],
    - a < b < c < d.

Примеры:
Ввод: numbers = [1,2,3,6]
Вывод: 1

Ввод: numbers = [3,3,6,4,5]
Вывод: 0
'''

from typing import List

def count_quadruplets(numbers: List[int]) -> int:
    quadruplet_count = 0
    numbers_array_length = len(numbers)

    for index_d in range(3, numbers_array_length):
        for index_c in range(2, index_d):
            for index_b in range(1, index_c):
                required_first_element_value = numbers[index_d] - (numbers[index_b] + numbers[index_c])
                for index_a in range(index_b):
                    if numbers[index_a] == required_first_element_value:
                        quadruplet_count += 1

    return quadruplet_count