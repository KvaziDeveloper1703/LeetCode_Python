'''
You are given an array of intervals, where intervals[i] = [startᵢ, endᵢ], and each startᵢ is unique.
For each interval i, the right interval is defined as an interval j such that: startⱼ >= endᵢ, and startⱼ is the smallest possible value that satisfies the above condition.

Return an array of indices — for each interval i, return the index j of its right interval. If no such interval j exists, return -1 for that position.

Examples:
Input: intervals = [[1,2]]
Output: [-1]

Input: intervals = [[3,4],[2,3],[1,2]]
Output: [-1, 0, 1]

Дан массив интервалов, где intervals[i] = [startᵢ, endᵢ], и все startᵢ — уникальны.
Для каждого интервала i найдите его правый интервал j, такой что: startⱼ >= endᵢ, и startⱼ — наименьшее возможное значение, удовлетворяющее этому условию.

Верните массив индексов: для каждого интервала i укажите индекс j его правого интервала. Если такого интервала не существует — поставьте -1 на этой позиции.

Примеры:
Ввод: intervals = [[1,2]]
Вывод: [-1]

Ввод: intervals = [[3,4],[2,3],[1,2]]
Вывод: [-1, 0, 1]
'''

def find_right_interval(intervals: list[list[int]]) -> list[int]:
    list_start_and_index = []

    for index in range(len(intervals)):
        start_point = intervals[index][0]
        list_start_and_index.append((start_point, index))

    list_start_and_index.sort()
    result_indices = []

    for interval in intervals:
        end_point = interval[1]
        minimal_index = -1

        for start_point, original_index in list_start_and_index:
            if start_point >= end_point:
                minimal_index = original_index
                break

        result_indices.append(minimal_index)

    return result_indices