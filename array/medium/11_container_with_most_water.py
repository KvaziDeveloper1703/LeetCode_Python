'''
You are given an array of integers height where each element represents the height of a vertical line drawn at that index. The endpoints of the i-th line are (i, 0) and (i, height[i]).
Find two lines such that together with the x-axis, they form a container that holds the most water.

Return the maximum amount of water the container can store.

Examples:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Input: height = [1,1]
Output: 1

Дан массив целых чисел height, где каждый элемент представляет высоту вертикальной линии, проведённой в соответствующей позиции. Концы i-й линии — это точки (i, 0) и (i, height[i]).
Найдите такие две линии, которые вместе с осью X образуют контейнер, способный удержать наибольшее количество воды.

Верните максимальный объём воды, который может вместить такой контейнер.

Примеры:
Ввод: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Вывод: 49

Ввод: height = [1, 1]
Вывод: 1
'''

from typing import List

def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        min_height = min(height[left], height[right])
        current_area = width * min_height
        max_area = max(max_area, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area