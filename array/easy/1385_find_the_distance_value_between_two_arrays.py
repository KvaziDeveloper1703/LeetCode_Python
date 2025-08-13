'''
Given two integer arrays array_1 and array_2, and an integer d.

The distance value is defined as the number of elements array_1[i] such that there is no element array_2[j] satisfying the condition: |array_1[i] - array_2[j]| <= d

That is:
    + For each element in array_1, check all elements in array_2;
    + If all absolute differences are greater than d, count this element;
    + Return the total count.

Examples:
Input:  array_1 = [4,5,8], array_2 = [10,9,1,8], d = 2
Output: 2

Input:  array_1 = [1,4,2,3], array_2 = [-4,-3,6,10,20,30], d = 3
Output: 2

Даны два целочисленных массива array_1 и array_2, а также целое число d.

Значение расстояния определяется как количество элементов array_1[i], для которых не существует элемента array_2[j], удовлетворяющего условию: |array_1[i] - array_2[j]| <= d

То есть:
    + Для каждого элемента из array_1 проверяем все элементы array_2;
    + Если все абсолютные разности больше d, этот элемент засчитывается;
    + Вернуть общее количество таких элементов.

Примеры:
Ввод:  array_1 = [4,5,8], array_2 = [10,9,1,8], d = 2
Вывод: 2

Ввод:  array_1 = [1,4,2,3], array_2 = [-4,-3,6,10,20,30], d = 3
Вывод: 2
'''

from bisect import bisect_left
from typing import List

def find_the_distance_value(array_1: List[int], array_2: List[int], d: int) -> int:
    array_2.sort()
    result = 0
    for x in array_1:
        i = bisect_left(array_2, x - d)
        if i == len(array_2) or array_2[i] > x + d:
            result += 1
    return result