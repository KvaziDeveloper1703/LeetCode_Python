'''
You are given an integer array numbers of even length.

You need to split the array into two subarrays numbers1 and numbers2 such that:
    - numbers1.length == numbers2.length == numbers.length / 2;
    - All elements in numbers1 are distinct;
    - All elements in numbers2 are distinct.

Return true if it is possible to split the array in this way, otherwise return false.

Examples:
Input: numbers = [1,1,2,2,3,4]
Output: true

Input: numbers = [1,1,1,1]
Output: false

Дан целочисленный массив numbers чётной длины.

Необходимо разбить массив на два подмассива numbers1 и numbers2 так, чтобы выполнялись следующие условия:
    - numbers1.length == numbers2.length == numbers.length / 2;
    - Все элементы массива numbers1 различны;
    - Все элементы массива numbers2 различны.

Верните true, если такое разбиение возможно, иначе верните false.

Примеры:
Ввод: numbers = [1,1,2,2,3,4]
Вывод: true

Ввод: numbers = [1,1,1,1]
Вывод: false
'''

from typing import List
from collections import Counter

def is_possible_to_split(numbers: List[int]) -> bool:
    frequencies = Counter(numbers)

    for count in frequencies.values():
        if count > 2:
            return False

    return True