'''
You are given an array height consisting of n non-negative integers. Each element represents the height of a vertical bar in an elevation map, and the width of each bar is 1.
After it rains, water may get trapped between the bars. Your task is to compute how many units of water can be trapped.

Examples:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Input: height = [4,2,0,3,2,5]
Output: 9

Дан массив height, состоящий из n неотрицательных целых чисел. Каждый элемент представляет высоту вертикального столбца на карте возвышений, при этом ширина каждого столбца равна 1.
После дождя между столбцами может скапливаться вода. Ваша задача — вычислить, сколько единиц воды может быть удержано между столбцами.

Примеры:
Ввод: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Вывод: 6

Ввод: height = [4,2,0,3,2,5]
Вывод: 9
'''

from typing import List

def trap(height: List[int]) -> int:
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water