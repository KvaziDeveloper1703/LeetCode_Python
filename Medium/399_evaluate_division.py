'''
You are given:
+ Equations like A / B = value;
+ Queries like C / D = ?.

Return the result of each query. If the answer can’t be determined, return -1.0.

Example:
Input: 
equations = [["a","b"],["b","c"]]
values = [2.0, 3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

Output:
[6.0, 0.5, -1.0, 1.0, -1.0]

Даны:
+ Список уравнений: equations[i] = [A, B], где A / B = values[i];
+ Список запросов: queries[j] = [C, D] — нужно найти C / D.

Верни список ответов на запросы. Если ответ определить нельзя, верни -1.0.

Пример:
Ввод:
equations = [["a","b"],["b","c"]]
values = [2.0, 3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

Вывод:
[6.0, 0.5, -1.0, 1.0, -1.0]
'''

from typing import List, Dict, Set
from collections import defaultdict

class Solution:
    def calc_equation(  self,
                        equations: List[List[str]],
                        values: List[float],
                        queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(Dict)
        for (numerator, denominator), value in zip(equations, values):
            graph[numerator][denominator] = value
            graph[denominator][numerator] = 1 / value

        def dfs(current: str, target: str, visited: Set[str]) -> float:
            if current not in graph or target not in graph:
                return -1.0
            if current == target:
                return 1.0
            visited.add(current)

            for neighbor, weight in graph[current].items():
                if neighbor in visited:
                    continue
                product = dfs(neighbor, target, visited)
                if product != -1.0:
                    return weight * product

            return -1.0

        result = []
        for start, end in queries:
            result.append(dfs(start, end, set()))
        return result