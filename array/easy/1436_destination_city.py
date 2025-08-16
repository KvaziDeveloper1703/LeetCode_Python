'''
Given an array paths, where paths[i] = [cityA, cityB] means there is a direct path going from cityA to cityB.

Return the destination city - the city that has no outgoing paths to another city.

It is guaranteed that the graph forms a straight line without cycles, so there will be exactly one destination city.

Examples:
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"

Дан массив paths, где paths[i] = [cityA, cityB] означает, что существует прямой путь из города cityA в город cityB.

Нужно вернуть город назначения — тот город, из которого нет исходящих путей в другие города.

Гарантируется, что граф образует прямую линию без циклов, поэтому будет существовать ровно один город назначения.

Примеры:
Ввод: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Вывод: "Sao Paulo"

Ввод: paths = [["B","C"],["D","B"],["C","A"]]
Вывод: "A"
'''

from typing import List

def destination_city(paths: List[List[str]]) -> str:
    departure_cities = set()
    for departure, arrival in paths:
        departure_cities.add(departure)

    for _, arrival in paths:
        if arrival not in departure_cities:
            return arrival

    return ""