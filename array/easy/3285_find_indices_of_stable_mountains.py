'''
There are n mountains in a row, and each mountain has a height.
You are given an integer array height, where height[i] is the height of mountain i, and an integer threshold.
A mountain is called stable if the mountain immediately before it has a height strictly greater than threshold.
Return an array containing the indices of all stable mountains.

Examples:
Input: height = [1, 2, 3, 4, 5], threshold = 2
Output: [3, 4]

Input: height = [10, 1, 10, 1, 10], threshold = 3
Output: [1, 3]

Дано n гор, стоящих в ряд, и у каждой горы есть высота.
Вам дан целочисленный массив height, где height[i] - высота горы i, а также целое число threshold.
Гора считается стабильной, если гора непосредственно перед ней имеет высоту строго больше threshold.
Верните массив индексов всех стабильных гор.

Примеры:
Ввод: height = [1, 2, 3, 4, 5], threshold = 2
Вывод: [3, 4]

Ввод: height = [10, 1, 10, 1, 10], threshold = 3
Вывод: [1, 3]
'''

from typing import List

def stable_mountains(height: List[int], threshold: int) -> List[int]:
    result = []

    for i in range(1, len(height)):
        if height[i - 1] > threshold:
            result.append(i)

    return result