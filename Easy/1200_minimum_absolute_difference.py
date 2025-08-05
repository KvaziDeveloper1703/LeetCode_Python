'''
Given an array of distinct integers my_array. You need to find all pairs of elements that have the minimum absolute difference between any two elements in the array.

Return a list of such pairs in ascending order.

Each pair [a, b] must satisfy:
    + a and b are from my_array;
    + a < b;
    + b - a equals the minimum absolute difference found in the array.

Examples:
Input: my_array = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]

Input: my_array = [1,3,6,10,15]
Output: [[1,3]]

Дан массив различных целых чисел my_array. Нужно найти все пары элементов, которые имеют минимальную абсолютную разницу среди всех пар элементов массива.

Верните список таких пар в порядке возрастания.

Каждая пара [a, b] должна удовлетворять условиям:
    + a и b взяты из my_array;
    + a < b;
    + b - a равно минимальной найденной абсолютной разнице.

Примеры:
Ввод: my_array = [4,2,1,3]
Вывод: [[1,2],[2,3],[3,4]]

Ввод: my_array = [1,3,6,10,15]
Вывод: [[1,3]]
'''

from typing import List

def minimum_abs_difference(my_array: List[int]) -> List[List[int]]:
    my_array.sort()
    min_diff = float('inf')
    for i in range(1, len(my_array)):
        diff = my_array[i] - my_array[i - 1]
        if diff < min_diff:
            min_diff = diff
    result = []
    for i in range(1, len(my_array)):
        if my_array[i] - my_array[i - 1] == min_diff:
            result.append([my_array[i - 1], my_array[i]])
    return result