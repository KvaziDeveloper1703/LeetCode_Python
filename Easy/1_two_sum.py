'''
Given an array of integers numbers and an integer target, return the indices of the two numbers such that they add up to the target.
You may assume that each input has exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Examples:
Input: numbers = [2,7,11,15], target = 9
Output: [0,1]

Input: numbers = [3,2,4], target = 6
Output: [1,2]

Дан массив целых чисел numbers и целевое число target. Необходимо вернуть индексы двух чисел из массива, сумма которых равна target.
Можно предположить, что для каждого входного набора существует ровно одно решение, и одно и то же число нельзя использовать дважды.
Ответ можно вернуть в любом порядке.

Примеры:
Ввод: numbers = [2, 7, 11, 15], target = 9
Вывод: [0, 1]

Ввод: numbers = [3, 2, 4], target = 6
Вывод: [1, 2]
'''

from typing import List

def two_sum(numbers: List[int], target: int) -> List[int]:
        numbers_dictionary = {}
        for i, number in enumerate(numbers):
            complement = target - number
            if complement in numbers_dictionary:
                return [numbers_dictionary[complement], i]
            numbers_dictionary[number] = i
        return []