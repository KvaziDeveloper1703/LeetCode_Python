'''
You are tasked with loading boxes onto a truck.

You are given a 2D array boxTypes, where each element is defined as: boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi], meaning:
    - numberOfBoxesi - the number of boxes of type i,
    - numberOfUnitsPerBoxi - the number of units in each box of that type.

You are also given an integer truckSize, which represents the maximum number of boxes the truck can carry.

You can choose boxes of any types as long as the total number of boxes does not exceed truckSize.

Return the maximum total number of units that can be loaded onto the truck.

Examples:
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8

Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91

Вам нужно загрузить некоторое количество коробок в грузовик.

Дан двумерный массив boxTypes, где каждый элемент описывает тип коробок: boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi], где:
    - numberOfBoxesi - количество коробок типа i,
    - numberOfUnitsPerBoxi - количество единиц в каждой коробке этого типа.

Также дано число truckSize - максимальное количество коробок, которое можно погрузить в грузовик.

Можно выбрать коробки любых типов, пока общее количество коробок не превышает truckSize.

Нужно вернуть максимальное общее количество единиц, которое можно погрузить в грузовик.

Примеры:
Ввод: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Вывод: 8

Ввод: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Вывод: 91
'''

from typing import List

def maximum_units(boxTypes: List[List[int]], truckSize: int) -> int:
    box_types_sorted = sorted(boxTypes, key=lambda item: item[1], reverse=True)
    remaining_truck_capacity = truckSize
    total_units_loaded = 0

    for number_of_boxes, number_of_units_per_box in box_types_sorted:
        if remaining_truck_capacity == 0:
            break
        boxes_to_load = min(number_of_boxes, remaining_truck_capacity)
        total_units_loaded += boxes_to_load * number_of_units_per_box
        remaining_truck_capacity -= boxes_to_load

    return total_units_loaded