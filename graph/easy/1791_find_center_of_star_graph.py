'''
You are given an undirected star graph with n nodes labeled from 1 to n.
A star graph is a graph that has one center node and exactly n - 1 edges.
Each edge connects the center node to every other node in the graph.

You are given a 2D integer array edges, where each element edges[i] = [uᵢ, vᵢ] represents an undirected edge between nodes uᵢ and vᵢ.

Return the center node of the star graph.

Examples:
Input: edges = [[1,2], [2,3], [4,2]]
Output: 2

Input: edges = [[1,2], [5,1], [1,3], [1,4]]
Output: 1

Дан неориентированный звёздный граф из n узлов, пронумерованных от 1 до n.
Звёздный граф - это граф, в котором есть один центральный узел и ровно n - 1 ребро, каж­дое из которых соединяет центр с каждым другим узлом.

Дан двумерный массив edges, где edges[i] = [uᵢ, vᵢ] означает наличие неориентированного ребра между вершинами uᵢ и vᵢ.

Нужно вернуть номер центрального узла звёздного графа.

Примеры:
Ввод: edges = [[1,2], [2,3], [4,2]]
Вывод: 2

Ввод: edges = [[1,2], [5,1], [1,3], [1,4]]
Вывод: 1
'''

from typing import List

def find_сenter(edges: List[List[int]]) -> int:
    first_edge_node1, first_edge_node2 = edges[0]
    second_edge_node1, second_edge_node2 = edges[1]

    if first_edge_node1 == second_edge_node1 or first_edge_node1 == second_edge_node2:
        return first_edge_node1
    return first_edge_node2