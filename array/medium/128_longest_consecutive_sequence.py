'''
Given an unsorted array of integers numbers.
Return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Examples:
Input: numbers = [100,4,200,1,3,2]
Output: 4

Input: numbers = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Дан неотсортированный массив целых чисел numbers.
Необходимо найти длину самой длинной последовательности подряд идущих чисел.
Вы должны реализовать алгоритм с временем работы O(n).

Примеры:
Ввод: numbers = [100, 4, 200, 1, 3, 2]
Вывод: 4

Ввод: numbers = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Вывод: 9
'''

from typing import List

def longest_consecutive(numbers: List[int]) -> int:
    if not numbers:
        return 0

    number_set = set(numbers)
    longest_sequence = 0

    for number in number_set:
        if number - 1 not in number_set:
            current_number = number
            current_length = 1

            while current_number + 1 in number_set:
                current_number += 1
                current_length += 1

            longest_sequence = max(longest_sequence, current_length)

    return longest_sequence