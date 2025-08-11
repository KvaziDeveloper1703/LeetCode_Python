'''
Given an integer array my_array. Sort the integers in ascending order based on the number of 1 bits in their binary representation.
If two or more integers have the same number of 1 bits, sort them by their numerical value in ascending order.

Return the sorted array.

Examples:
Input: my_array = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]

Input: my_array = [1024,512,256,128,64,32,16,8,4,2,1]
Output: [1,2,4,8,16,32,64,128,256,512,1024]

Дан массив целых чисел my_array. Отсортируйте числа по возрастанию в зависимости от количества единиц в их двоичной записи.
Если два или более числа имеют одинаковое количество единиц, сортируйте их по значению в порядке возрастания.

Верните отсортированный массив.

Примеры:
Ввод: my_array = [0,1,2,3,4,5,6,7,8]
Вывод: [0,1,2,4,8,3,5,6,7]

Ввод: my_array = [1024,512,256,128,64,32,16,8,4,2,1]
Вывод: [1,2,4,8,16,32,64,128,256,512,1024]
'''

from typing import List

def sort_by_bits(numbers: List[int]) -> List[int]:
    return sorted(numbers, key=lambda number: (number.bit_count(), number))