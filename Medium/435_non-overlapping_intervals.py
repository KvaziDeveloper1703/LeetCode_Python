'''
Given an array of intervals intervals, where intervals[i] = [startᵢ, endᵢ], return the minimum number of intervals you need to remove so that the remaining intervals are non-overlapping.
Note: Intervals that only touch at a point are non-overlapping.

Examples:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2

Дан массив интервалов intervals, где intervals[i] = [startᵢ, endᵢ]. Верните минимальное количество интервалов, которые нужно удалить, чтобы оставшиеся интервалы не пересекались.
Примечание: Интервалы, которые касаются только в одной точке, считаются непересекающимися.

Примеры:
Ввод: intervals = [[1,2],[2,3],[3,4],[1,3]]
Вывод: 1

Ввод: intervals = [[1,2],[1,2],[1,2]]
Вывод: 2
'''

def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    count_non_overlap = 0        
    end = float('-inf')

    for interval in intervals:
        if interval[0] >= end:
            count_non_overlap += 1
            end = interval[1]

    return len(intervals) - count_non_overlap