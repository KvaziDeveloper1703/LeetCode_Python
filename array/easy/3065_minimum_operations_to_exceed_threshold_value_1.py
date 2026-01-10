'''
You are given a 0-indexed integer array numbers and an integer k.
In one operation, you may remove one occurrence of the smallest element in the array numbers.
Return the minimum number of operations required so that all elements of the array are greater than or equal to k.

Examples:
Input: numbers = [2,11,10,1,3], k = 10
Output: 3

Input: numbers = [1,1,2,4,9], k = 1
Output: 0

Дан 0-индексированный целочисленный массив numbers и целое число k.
За одну операцию можно удалить одно вхождение наименьшего элемента массива numbers.
Верните минимальное количество операций, необходимое для того, чтобы все элементы массива были больше либо равны k.

Примеры:
Ввод: numbers = [2,11,10,1,3], k = 10
Вывод: 3

Ввод: numbers = [1,1,2,4,9], k = 1
Вывод: 0
'''

from typing import List

def min_operations(numbers: List[int], k: int) -> int:
    operations_count = 0

    for value in numbers:
        if value < k:
            operations_count += 1

    return operations_count