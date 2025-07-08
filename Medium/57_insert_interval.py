'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [start_index, end_index] represent the start and the end of the ith interval. 
The intervals are sorted in ascending order by start_index. 
You are also given an interval new_interval = [start, end] that represents the start and end of another interval.

Insert new_interval into intervals such that intervals is still sorted in ascending order by start_index and there are no overlapping intervals.

Return the updated intervals after the insertion. Note that you don't need to modify intervals in-place. You can create a new array and return it.

Examples:
Input: intervals = [[1,3],[6,9]], new_interval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], new_interval = [4,8]
Output: [[1,2],[3,10],[12,16]]

Дан массив непересекающихся интервалов intervals, где intervals[i] = [начало, конец] — это начало и конец i-го интервала. 
Интервалы отсортированы по возрастанию начала. 
Также дан новый интервал new_interval = [start, end], который нужно вставить в массив.

Вставьте new_interval в intervals так, чтобы:
    + Массив остался отсортированным по началу интервала;
    + В итоговом массиве не было пересекающихся интервалов — объедините перекрывающиеся, если потребуется.

Верните обновлённый массив интервалов после вставки.

Примеры:
Ввод: intervals = [[1, 3], [6, 9]], new_interval = [2, 5]
Вывод: [[1, 5], [6, 9]]

Ввод: intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], new_interval = [4, 8]
Вывод: [[1, 2], [3, 10], [12, 16]]
'''

from typing import List

def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    result = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    result.append(new_interval)

    while i < n:
        result.append(intervals[i])
        i += 1
        
    return result