'''
A school wants to take an annual photo of all students. The students must stand in a single line in non-decreasing order of their heights.
The correct arrangement is represented by an integer array expected, where expected[i] is the height of the i-th student in the correctly ordered line.

Given an integer array heights representing the current order of students in line, where heights[i] is the height of the i-th student.

Return the number of indices where heights[i] is not equal to expected[i].

Examples:
Input: heights = [1,1,4,2,1,3]  
Output: 3  

Input: heights = [5,1,2,3,4]  
Output: 5

Школа хочет сделать ежегодную фотографию всех учеников. Ученики должны выстроиться в одну линию в неубывающем порядке по росту.
Правильная расстановка представлена целочисленным массивом expected, где expected[i] — это рост i-го ученика в правильно выстроенной линии.

Дан целочисленный массив heights, который отражает текущий порядок учеников в линии, где heights[i] — рост i-го ученика.

Вернуть количество индексов, для которых heights[i] не равно expected[i].

Примеры:
Ввод: heights = [1,1,4,2,1,3]  
Вывод: 3  

Ввод: heights = [5,1,2,3,4]  
Вывод: 5
'''

from typing import List

def height_checker(heights: List[int]) -> int:
    expected = sorted(heights)
    count = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            count += 1
    return count