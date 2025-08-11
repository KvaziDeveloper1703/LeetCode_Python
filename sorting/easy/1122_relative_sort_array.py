'''
Given two arrays, array_1 and array_2.
    + All elements of array_2 are distinct;
    + All elements in array_2 are also present in array_1.

Sort the elements of array_1 so that:
    1) The relative order of the elements that appear in array_2 matches the order of those elements in array_2;
    2) Elements that are not in array_2 appear at the end of array_1 in ascending order.

Examples:
Input: array_1 = [2,3,1,3,2,4,6,7,9,2,19], array_2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

Input: array_1 = [28,6,22,8,44,17], array_2 = [22,28,8,6]
Output: [22,28,8,6,17,44]

Даны два массива array_1 и array_2.
    + Все элементы массива array_2 различны;
    + Все элементы из array_2 также встречаются в array_1.

Нужно отсортировать array_1 так, чтобы:
    1) Порядок элементов, которые есть в array_2, совпадал с порядком этих элементов в array_2;
    2) Элементы, которых нет в array_2, должны быть размещены в конце array_1 в порядке возрастания.

Примеры:
Ввод: array_1 = [2,3,1,3,2,4,6,7,9,2,19], array_2 = [2,1,4,3,9,6]
Вывод: [2,2,2,1,4,3,3,9,6,7,19]

Ввод: array_1 = [28,6,22,8,44,17], array_2 = [22,28,8,6]
Вывод: [22,28,8,6,17,44]
'''

from typing import List

def relative_sort_array(array_1: List[int], array_2: List[int]) -> List[int]:
    element_to_index_mapping = {}
    for index, value in enumerate(array_2):
        element_to_index_mapping[value] = index

    def sort_key(element: int):
        if element in element_to_index_mapping:
            return (element_to_index_mapping[element], element)
        else:
            return (len(array_2), element)

    sorted_array = sorted(array_1, key=sort_key)
    return sorted_array