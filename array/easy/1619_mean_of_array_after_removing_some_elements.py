'''
Given an integer array named array.

Remove the smallest 5% of the elements and the largest 5% of the elements.

Then, return the mean of the remaining numbers.

The answer is accepted if it is within 10^-5 of the correct value.

Examples:
Input: array = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
Output: 2.00000

Input: arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
Output: 4.00000

Дан массив целых чисел array.

Удалите наименьшие 5% элементов массива и наибольшие 5% элементов массива. После этого верните среднее арифметическое оставшихся чисел.

Ответ считается правильным, если он отличается от верного не более чем на 10^-5.

Примеры:
Ввод: array = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
Вывод: 2.00000

Ввод: array = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
Вывод: 4.00000
'''

from typing import List

def trim_mean(array: List[int]) -> float:
    n = len(array)
    remove_count = n * 5 // 100

    array.sort()
    trimmed = array[remove_count : n - remove_count]

    mean_value = sum(trimmed) / len(trimmed)
    return mean_value