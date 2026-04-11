'''
Given an array of integers heights representing the heights of bars in a histogram (where the width of each bar is 1).
Return the area of the largest rectangle that can be formed inside the histogram.

Examples:
Input: heights = [2,1,5,6,2,3]
Output: 10

Input: heights = [2,4]
Output: 4

Дан массив целых чисел heights, который представляет высоты столбцов в гистограмме (при этом ширина каждого столбца равна 1).
Нужно найти площадь наибольшего прямоугольника, который можно вписать в эту гистограмму.

Примеры:
Ввод: heights = [2,1,5,6,2,3]
Вывод: 10

Ввод: heights = [2,4]
Вывод: 4
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