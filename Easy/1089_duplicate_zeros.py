'''
Given a fixed-length integer array my_array.

Duplicate each occurrence of 0, shifting the remaining elements to the right.

Examples:
Input: my_array = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]

Input: my_array = [1,2,3]
Output: [1,2,3]

Дан массив целых чисел фиксированной длины my_array.

Продублируйте каждое вхождение числа 0, сдвинув оставшиеся элементы вправо.

Примеры:
Ввод: my_array = [1,0,2,3,0,4,5,0]  
Вывод: [1,0,0,2,3,0,0,4]  

Ввод: my_array = [1,2,3]  
Вывод: [1,2,3]
'''

from typing import List

def duplicate_zeros(my_array: List[int]) -> None:
    n = len(my_array)
    i = 0
    while i < n:
        if my_array[i] == 0:
            my_array.pop()
            my_array.insert(i, 0)
            i += 1
        i += 1