'''
You are given a 1-indexed array of distinct integers numbers of length n.

You need to distribute all elements of numbers between two arrays arr1 and arr2 using exactly n operations.

Rules of distribution:
    - In the first operation, append numbers[1] to arr1;
    - In the second operation, append numbers[2] to arr2;
    - For every operation i where i ≥ 3:
        - If the last element of arr1 is greater than the last element of arr2, append numbers[i] to arr1;
        - Otherwise, append numbers[i] to arr2.

After all operations are completed, form the array result by concatenating arr1 and arr2: result = arr1 + arr2.
Return the array result.

Examples:
Input: numbers = [2, 1, 3]
Output: [2, 3, 1]

Input: numbers = [5, 4, 3, 8]
Output: [5, 3, 4, 8]

Вам дан 1-индексированный массив различных целых чисел numbers длины n.

Необходимо распределить все элементы массива numbers между двумя массивами arr1 и arr2, выполнив ровно n операций.

Правила распределения:
    - В первой операции добавить numbers[1] в arr1;
    - Во второй операции добавить numbers[2] в arr2;
    - В каждой операции с номером i, где i ≥ 3:
        - Если последний элемент arr1 больше последнего элемента arr2, добавить numbers[i] в arr1;
        - В противном случае добавить numbers[i] в arr2.

После выполнения всех операций сформировать массив result, объединив массивы arr1 и arr2: result = arr1 + arr2.
Верните массив result.

Примеры:
Ввод: numbers = [2, 1, 3]
Вывод: [2, 3, 1]

Ввод: numbers = [5, 4, 3, 8]
Вывод: [5, 3, 4, 8]
'''

from typing import List

def result_array(numbers: List[int]) -> List[int]:
    first_array = [numbers[0]]
    second_array = [numbers[1]]

    for index in range(2, len(numbers)):
        if first_array[-1] > second_array[-1]:
            first_array.append(numbers[index])
        else:
            second_array.append(numbers[index])

    return first_array + second_array