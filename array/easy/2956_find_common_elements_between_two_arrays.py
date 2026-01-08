'''
You are given two integer arrays numbers1 and numbers2 of lengths n and m, respectively.

Calculate the following values:
    - answer1 - the number of indices i such that the element numbers1[i] appears in the array numbers2;
    - answer2 - the number of indices i such that the element numbers2[i] appears in the array numbers1.

Return an array [answer1, answer2].

Examples:
Input:  numbers1 = [2, 3, 2], numbers2 = [1, 2]
Output: [2, 1]

Input:  numbers1 = [4, 3, 2, 3, 1], numbers2 = [2, 2, 5, 2, 3, 6]
Output: [3, 4]

Даны два целочисленных массива numbers1 и numbers2 длины n и m соответственно.

Необходимо вычислить следующие значения:
    - answer1 - количество индексов i, для которых элемент numbers1[i] присутствует в массиве numbers2;
    - answer2 - количество индексов i, для которых элемент numbers2[i] присутствует в массиве numbers1.

Верните массив [answer1, answer2].

Примеры:
Ввод:  numbers1 = [2, 3, 2], numbers2 = [1, 2]
Вывод: [2, 1]

Ввод:  numbers1 = [4, 3, 2, 3, 1], numbers2 = [2, 2, 5, 2, 3, 6]
Вывод: [3, 4]
'''

from typing import List

def find_intersection_values(numbers1: List[int], numbers2: List[int]) -> List[int]:
    set1 = set(numbers1)
    set2 = set(numbers2)

    answer1 = 0
    for x in numbers1:
        if x in set2:
            answer1 += 1

    answer2 = 0
    for x in numbers2:
        if x in set1:
            answer2 += 1

    return [answer1, answer2]