'''
Given an integer array my_array sorted in non-decreasing order.

There is exactly one integer in the array that appears more than 25% of the time. Return that integer.

Examples:
Input: my_array = [1, 2, 2, 6, 6, 6, 6, 7, 10]
Output: 6

Input: my_array = [1, 1]
Output: 1

Дан массив целых чисел my_array, отсортированный в неубывающем порядке.

В массиве ровно одно число встречается более чем в 25% случаев. Верните это число.

Примеры:
Ввод: my_array = [1, 2, 2, 6, 6, 6, 6, 7, 10]
Вывод: 6

Ввод: my_array = [1, 1]
Вывод: 1
'''

from typing import List

def find_special_integer(my_array: List[int]) -> int:
    threshold = len(my_array) // 4
    for i in range(len(my_array) - threshold):
        if my_array[i] == my_array[i + threshold]:
            return my_array[i]