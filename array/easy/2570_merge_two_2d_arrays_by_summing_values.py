'''
You are given two 2D integer arrays numbers1 and numbers2.
    - numbers1[i] = [id_i, value_i] means that the number with ID id_i has a value equal to value_i;
    - numbers2[i] = [id_i, value_i] means that the number with ID id_i has a value equal to value_i.

Each array:
    - contains unique IDs;
    - is sorted in ascending order by ID.

Merge the two arrays into a single array that is sorted in ascending order by ID, following these rules:
    - Include only those IDs that appear in at least one of the two arrays;
    - Each ID must appear exactly once in the result;
    - The value for each ID is the sum of its values from both arrays;
    - If an ID does not exist in one of the arrays, its value in that array is considered to be 0.

Return the resulting array.

Examples:
Input: numbers1 = [[1,2],[2,3],[4,5]], numbers2 = [[1,4],[3,2],[4,1]]
Output: [[1,6],[2,3],[3,2],[4,6]]

Input: numbers1 = [[2,4],[3,6],[5,5]], numbers2 = [[1,3],[4,3]]
Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]

Вам даны два двумерных целочисленных массива numbers1 и numbers2.
    - numbers1[i] = [id_i, value_i] означает, что числу с идентификатором id_i соответствует значение value_i;
    - numbers2[i] = [id_i, value_i] означает, что числу с идентификатором id_i соответствует значение value_i.

Каждый массив:
    - содержит уникальные идентификаторы;
    - отсортирован по возрастанию идентификаторов.

Объедините два массива в один массив, также отсортированный по возрастанию идентификаторов, соблюдая следующие условия:
    - В результирующий массив включаются только те идентификаторы, которые присутствуют хотя бы в одном из массивов;
    - Каждый идентификатор должен присутствовать ровно один раз;
    - Значение каждого идентификатора равно сумме значений из обоих массивов;
    - Если идентификатор отсутствует в одном из массивов, его значение в этом массиве считается равным 0.

Верните полученный массив.

Примеры:
Ввод: numbers1 = [[1,2],[2,3],[4,5]], numbers2 = [[1,4],[3,2],[4,1]]
Вывод: [[1,6],[2,3],[3,2],[4,6]]

Ввод: numbers1 = [[2,4],[3,6],[5,5]], numbers2 = [[1,3],[4,3]]
Вывод: [[1,3],[2,4],[3,6],[4,3],[5,5]]
'''

from typing import List

def merge_arrays(numbers1: List[List[int]], numbers2: List[List[int]]) -> List[List[int]]:
    index_first = 0
    index_second = 0
    merged_array = []

    while index_first < len(numbers1) and index_second < len(numbers2):
        id_first, value_first = numbers1[index_first]
        id_second, value_second = numbers2[index_second]

        if id_first == id_second:
            merged_array.append([id_first, value_first + value_second])
            index_first += 1
            index_second += 1
        elif id_first < id_second:
            merged_array.append([id_first, value_first])
            index_first += 1
        else:
            merged_array.append([id_second, value_second])
            index_second += 1

    while index_first < len(numbers1):
        merged_array.append(numbers1[index_first])
        index_first += 1

    while index_second < len(numbers2):
        merged_array.append(numbers2[index_second])
        index_second += 1

    return merged_array