'''
You are given two 2D integer arrays, items1 and items2, each representing a collection of items.

Each item is described as:
    - items[i] = [value_i, weight_i]
where:
    - value_i is the value of the item,
    - weight_i is the weight of the item.

The value of each item is unique within each array.

Your task is to merge the two arrays by summing the weights of items that have the same value.

Return a 2D integer array ret such that: ret[i] = [value_i, total_weight_i] where total_weight_i is the sum of the weights of all items with value value_i from both items1 and items2.

The resulting array ret must be returned in ascending order by value.

Examples:
Input: items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
Output: [[1,6],[3,9],[4,5]]

Input: items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]
Output: [[1,4],[2,4],[3,4]]

Вам даны два двумерных целочисленных массива items1 и items2, каждый из которых представляет набор предметов.

Каждый предмет описывается в формате:
    - items[i] = [value_i, weight_i]
где:
    - value_i - значение предмета,
    - weight_i - вес предмета.

Значения предметов в каждом массиве уникальны.

Необходимо объединить два массива, суммируя веса предметов с одинаковым значением.

Верните двумерный массив ret, где: ret[i] = [value_i, total_weight_i] а total_weight_i — это сумма весов всех предметов со значением value_i, взятых из массивов items1 и items2.

Итоговый массив ret должен быть отсортирован по возрастанию значения value.

Примеры:
Ввод: items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
Вывод: [[1,6],[3,9],[4,5]]

Ввод: items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]
Вывод: [[1,4],[2,4],[3,4]]
'''

from typing import List

def merge_similar_items(items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
    values_to_weight = {}

    for value, weight in items1:
        if value in values_to_weight:
            values_to_weight[value] += weight
        else:
            values_to_weight[value] = weight

    for value, weight in items2:
        if value in values_to_weight:
            values_to_weight[value] += weight
        else:
            values_to_weight[value] = weight

    result = []
    for value in sorted(values_to_weight):
        result.append([value, values_to_weight[value]])

    return result