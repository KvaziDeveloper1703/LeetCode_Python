'''
You are given two 0-indexed integer arrays numbers1 and numbers2.

Return an array answer of size 2 where:
    - answer[0] is a list of all distinct integers in numbers1 that do not appear in numbers2;
    - answer[1] is a list of all distinct integers in numbers2 that do not appear in numbers1.

The integers in the lists may be returned in any order.

Examples:
Input: numbers1 = [1,2,3], numbers2 = [2,4,6]
Output: [[1,3], [4,6]]

Input: numbers1 = [1,2,3,3], numbers2 = [1,1,2,2]
Output: [[3], []]

Даны два массива целых чисел numbers1 и numbers2, индексируемые с нуля.

Нужно вернуть массив answer длиной 2, где:
    - answer[0] содержит все уникальные числа из numbers1, которые не встречаются в numbers2;
    - answer[1] содержит все уникальные числа из numbers2, которые не встречаются в numbers1.

Порядок элементов может быть любым.

Примеры:
Ввод: numbers1 = [1,2,3], numbers2 = [2,4,6]
Вывод: [[1,3], [4,6]]

Ввод: numbers1 = [1,2,3,3], numbers2 = [1,1,2,2]
Вывод: [[3], []]
'''

from typing import List

def find_difference(numbers1: List[int], numbers2: List[int]) -> List[List[int]]:
    set1 = set(numbers1)
    set2 = set(numbers2)

    unique_in_numbers1 = list(set1 - set2)
    unique_in_numbers2 = list(set2 - set1)

    return [unique_in_numbers1, unique_in_numbers2]