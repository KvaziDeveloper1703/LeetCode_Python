'''
Given two integer arrays numbers and index.

Rules to create the target array:
    1) Start with an empty array target;
    2) Iterate from left to right through numbers[i] and index[i];
    3) Insert the value numbers[i] into target at position index[i];
    4) Repeat until all elements from numbers and index are processed.

Return the final target array.

It is guaranteed that all insert operations will be valid.

Examples:
Input: numbers = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]

Input: numbers = [1,2,3,4,0], index = [0,1,2,3,0]
Output: [0,1,2,3,4]

Даны два целочисленных массива numbers и index.

Правила создания массива target:
    1) Начните с пустого массива target;
    2) Двигайтесь слева направо по элементам numbers[i] и index[i];
    3) Вставьте значение numbers[i] в массив target на позицию index[i];
    4) Повторяйте, пока не обработаете все элементы из numbers и index.

Верните итоговый массив target.

Гарантируется, что все операции вставки будут корректными.

Примеры:
Ввод:  numbers = [0,1,2,3,4], index = [0,1,2,2,1]
Вывод: [0,4,1,3,2]

Ввод:  numbers = [1,2,3,4,0], index = [0,1,2,3,0]
Вывод: [0,1,2,3,4]
'''

from typing import List

def create_target_array(numbers: List[int], index: List[int]) -> List[int]:
    target_array: List[int] = []
    for current_number, desired_position in zip(numbers, index):
        target_array.insert(desired_position, current_number)
    return target_array