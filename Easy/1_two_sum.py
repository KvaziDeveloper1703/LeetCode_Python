'''
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.
You may assume that each input has exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Examples:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]

Дан массив целых чисел nums и целевое число target. Необходимо вернуть индексы двух чисел из массива, сумма которых равна target.
Можно предположить, что для каждого входного набора существует ровно одно решение, и одно и то же число нельзя использовать дважды.
Ответ можно вернуть в любом порядке.

Примеры:
Ввод: nums = [2, 7, 11, 15], target = 9
Вывод: [0, 1]

Ввод: nums = [3, 2, 4], target = 6
Вывод: [1, 2]

Ввод: nums = [3, 3], target = 6
Вывод: [0, 1]
'''

from typing import List

def two_sum(given_numbers: List[int], given_target: int) -> List[int]:
        numbers_dictionary = {}

        for i, number in enumerate(given_numbers):
            complement = given_target - number

            if complement in numbers_dictionary:
                return [numbers_dictionary[complement], i]

            numbers_dictionary[number] = i

        return []