'''
Given an array of intervals where intervals[i] = [start_index, end_index], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Examples:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]

Дан массив интервалов, где intervals[i] = [начало, конец]. Необходимо объединить все перекрывающиеся интервалы и вернуть массив неперекрывающихся интервалов, которые полностью покрывают все интервалы из исходного массива.

Примеры:
Ввод: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Вывод: [[1, 6], [8, 10], [15, 18]]

Ввод: intervals = [[1, 4], [4, 5]]
Вывод: [[1, 5]]
'''

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged