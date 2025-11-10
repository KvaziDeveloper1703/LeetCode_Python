'''
You are given:
- an array of distinct integers my_array, and
- an array of integer arrays pieces, where all integers across pieces are distinct.

Your goal is to form the array my_array by concatenating the arrays from pieces in any order. However, you cannot change the order of numbers inside each subarray pieces[i].

Return True if it is possible to form the array my_array from the arrays in pieces. Otherwise, return False.

Examples:
Input: my_array = [15,88], pieces = [[88],[15]]
Output: True

Input: my_array = [49,18,16], pieces = [[16,18,49]]
Output: False

Даны:
- массив различных целых чисел my_array,
- и массив массивов целых чисел pieces, где все числа также уникальны между собой.

Нужно определить, можно ли собрать массив my_array, склеивая подмассивы из pieces в любом порядке, но не меняя порядок элементов внутри каждого подмассива pieces[i].

Если это возможно — вернуть True, иначе — False.

Примеры:
Ввод: my_array = [15,88], pieces = [[88],[15]]
Вывод: True

Ввод: my_array = [49,18,16], pieces = [[16,18,49]]
Вывод: False
'''

from typing import List

def can_form_array(self, my_array: List[int], pieces: List[List[int]]) -> bool:
    index_map = {piece[0]: piece for piece in pieces}
    i = 0

    while i < len(my_array):
        if my_array[i] not in index_map:
            return False
        piece = index_map[my_array[i]]
        for number in piece:
            if i >= len(my_array) or my_array[i] != number:
                return False
            i += 1

    return True