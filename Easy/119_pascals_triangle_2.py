'''
Given an integer row_index, return the row_indexᵗʰ (0-indexed) row of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Examples:
Input: row_index = 3
Output: [1,3,3,1]

Input: row_index = 0
Output: [1]

Дано целое число row_index. Верните строку с индексом row_index (нумерация с 0) из треугольника Паскаля.
В треугольнике Паскаля каждое число — это сумма двух чисел, находящихся непосредственно над ним.

Примеры:
Ввод: row_index = 3
Вывод: [1,3,3,1]

Ввод: row_index = 0
Вывод: [1]
'''

from typing import List

def get_row(row_index: int) -> List[int]:
    row = [1]
    for i in range(1, row_index + 1):
        new_row = [1] * (i + 1)
        for j in range(1, i):
            new_row[j] = row[j - 1] + row[j]
        row = new_row
    return row