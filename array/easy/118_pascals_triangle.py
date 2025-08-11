'''
Given an integer number_of_rows, return the first number_of_rows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Examples:
Input: number_of_rows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Input: number_of_rows = 1
Output: [[1]]

Дано целое число number_of_rows. Верните первые num_rows строк треугольника Паскаля.
В треугольнике Паскаля каждое число — это сумма двух чисел, находящихся непосредственно над ним.

Пример:
Ввод: number_of_rows = 5
Вывод: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Ввод: number_of_rows = 1
Вывод: [[1]]
'''

from typing import List

def generate(number_of_rows: int) -> List[List[int]]:
    triangle = []

    for i in range(number_of_rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle