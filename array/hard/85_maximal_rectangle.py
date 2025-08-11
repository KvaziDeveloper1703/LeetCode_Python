'''
Given a rows x columns binary matrix filled with '0's and '1's, find the largest rectangle containing only '1's and return its area.

Examples:
Input: matrix = [   ["1","0","1","0","0"],
                    ["1","0","1","1","1"],
                    ["1","1","1","1","1"],
                    ["1","0","0","1","0"]
            ]
Output: 6

Input: matrix = [["0"]]
Output: 0

Дана бинарная матрица размера rows x columns, заполненная символами '0' и '1'.
Найдите наибольший прямоугольник, состоящий только из '1', и верните его площадь.

Примеры:
Ввод: matrix = [["1","0","1","0","0"],
                ["1","0","1","1","1"],
                ["1","1","1","1","1"],
                ["1","0","0","1","0"]
            ]
Вывод: 6

Ввод: 
matrix = [["0"]]
Вывод: 0
'''

from typing import List

def largest_rectangle_area(heights: List[int]) -> int:
    stack = []
    max_area = 0
    n = len(heights)

    for i in range(n + 1):
        current_height = 0 if i == n else heights[i]

        while stack and current_height < heights[stack[-1]]:
            top_index = stack.pop()
            height = heights[top_index]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        stack.append(i)

    return max_area

def maximal_rectangle(matrix: List[List[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    
    n_columns = len(matrix[0])
    heights = [0] * n_columns
    max_area = 0

    for row in matrix:
        for idx, value in enumerate(row):
            if value == '1':
                heights[idx] += 1
            else:
                heights[idx] = 0

        max_area = max(max_area, largest_rectangle_area(heights))
        
    return max_area