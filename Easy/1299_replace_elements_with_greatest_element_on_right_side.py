'''
Given an integer array my_array, replace each element with the greatest element among the elements to its right, and replace the last element with -1.

Return the modified array.

Examples:
Input: my_array = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

Input: my_array = [400]
Output: [-1]

Дан массив целых чисел my_array. Замените каждый элемент массива на наибольший элемент среди тех, что находятся справа от него. Последний элемент массива всегда заменяется на -1.

Верните изменённый массив.

Примеры:
Ввод: my_array = [17,18,5,4,6,1]
Вывод: [18,6,6,6,1,-1]

Ввод: my_array = [400]
Вывод: [-1]
'''

from typing import List

def replace_elements(my_array: List[int]) -> List[int]:
    max_right = -1
    for i in range(len(my_array) - 1, -1, -1):
        new_value = max_right
        max_right = max(max_right, my_array[i])
        my_array[i] = new_value
    return my_array