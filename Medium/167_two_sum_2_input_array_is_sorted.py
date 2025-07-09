'''
You are given a 1-indexed array of integers numbers that is sorted in non-decreasing order. 
Your task is to find two numbers in the array such that they add up to a given target.
Let these two numbers be numbers[index_1] and numbers[index_2] where 1 <= index_1 < index_2 <= numbers.length.

Return the indices of the two numbers as an array [index_1, index_2]. The indices should be 1-based.

Examples:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Input: numbers = [2,3,4], target = 6
Output: [1,3]

Дан массив целых чисел numbers с индексацией с 1. Массив отсортирован по неубыванию.
Ваша задача — найти два числа в массиве, сумма которых равна заданному числу target.
Пусть эти два числа — это numbers[index_1] и numbers[index_2], где выполняется условие: 1 <= index_1 < index_2 <= numbers.length.

Верните индексы этих двух чисел в виде массива [index_1, index_2]. Индексы должны быть 1-based.

Примеры:
Ввод: numbers = [2, 7, 11, 15], target = 9
Вывод: [1, 2]

Ввод: numbers = [2, 3, 4], target = 6
Вывод: [1, 3]
'''

from typing import List

def two_sum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []