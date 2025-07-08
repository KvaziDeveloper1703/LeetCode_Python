'''
You are given an m x n integer matrix with the following two properties:
    + Each row is sorted in non-decreasing order;
    + The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return True if target is in the matrix, and False otherwise.

You must implement a solution with O(log(m * n)) time complexity.

Example:
Input: matrix = [   [1,3,5,7],
                    [10,11,16,20],
                    [23,30,34,60]
            ], target = 3  
Output: True

Вам дана целочисленная матрица размера m x n, обладающая следующими свойствами:
    + Каждая строка отсортирована по неубыванию;
    + Первый элемент каждой строки больше последнего элемента предыдущей строки.

Дан целочисленный target. Необходимо определить, содержится ли target в матрице. Верните True, если элемент найден, и False в противном случае.
Требуется реализовать алгоритм с временной сложностью O(log(m * n)).

Пример:
Ввод: matrix = [[1,3,5,7],
                [10,11,16,20],
                [23,30,34,60]
            ], target = 3  
Вывод: True
'''

from typing import List

def search_matrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        middle = (left + right) // 2
        middle_value = matrix[middle // n][middle % n]

        if middle_value == target:
            return True
        elif middle_value < target:
            left = middle + 1
        else:
            right = middle - 1

    return False