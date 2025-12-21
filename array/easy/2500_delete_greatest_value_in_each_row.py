'''
You are given an m × n matrix grid consisting of positive integers.

Perform the following operation repeatedly until the matrix becomes empty:
    - From each row, remove the element with the maximum value. If there are multiple elements with the same maximum value, you may remove any one of them;
    - Among all removed elements in the current operation, find the maximum value and add it to the answer.

After each operation, the number of columns in the matrix decreases by one.

Return the final value of the answer after all operations are completed.

Examples:
Input: grid = [[1, 2, 4], [3, 3, 1]]
Output: 8

Input: grid = [[10]]
Output: 10

Дана матрица grid размера m × n, состоящая из положительных целых чисел.

Необходимо выполнять следующую операцию до тех пор, пока матрица не станет пустой:
    - Из каждой строки удаляется элемент с наибольшим значением. Если таких элементов несколько, можно удалить любой из них;
    - Среди всех удалённых элементов текущей операции выбирается максимальный, и его значение прибавляется к ответу.

После каждой операции количество столбцов в матрице уменьшается на один.

Верните итоговое значение ответа после выполнения всех операций.

Примеры:
Ввод: grid = [[1, 2, 4], [3, 3, 1]]
Вывод: 8

Ввод: grid = [[10]]
Вывод: 10
'''

from typing import List

def delete_greatest_value(grid: List[List[int]]) -> int:
    for row in grid:
        row.sort()

    total_sum = 0
    number_of_columns = len(grid[0])

    for column_index in range(number_of_columns):
        maximum_deleted_value = 0
        for row in grid:
            maximum_deleted_value = max(maximum_deleted_value, row[column_index])
        total_sum += maximum_deleted_value

    return total_sum