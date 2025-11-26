'''
You are given an undirected graph with n vertices, labeled from 0 to n – 1.
The edges are provided as a 2D integer array edges, where each edges[i] = [uᵢ, vᵢ] represents an undirected edge between vertices uᵢ and vᵢ.
There is at most one edge between any pair of vertices, and no vertex has an edge to itself.

Your task is to determine whether there exists a valid path from the vertex source to the vertex destination.

Given n, edges, source, and destination, return True if such a path exists, and False otherwise.

Examples:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: True

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: False

Дан неориентированный граф с n вершинами, пронумерованными от 0 до n - 1.
Рёбра графа заданы в виде двумерного массива edges, где каждая запись edges[i] = [uᵢ, vᵢ] обозначает неориентированное ребро между вершинами uᵢ и vᵢ.
Между любой парой вершин может быть не более одного ребра, и ни одна вершина не соединена ребром сама с собой.

Нужно определить, существует ли путь от вершины source к вершине destination.

По данным n, edges, source и destination верните True, если такой путь существует, и False - если нет.

Примеры:
Ввод: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Вывод: True

Ввод: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Вывод: False
'''

from typing import List

def valid_path(number_of_vertices: int, edges: List[List[int]], source_vertex: int, destination_vertex: int) -> bool:
    if source_vertex == destination_vertex:
        return True

    adjacency_list = [[] for vertex_index in range(number_of_vertices)]
    for first_vertex, second_vertex in edges:
        adjacency_list[first_vertex].append(second_vertex)
        adjacency_list[second_vertex].append(first_vertex)

    visited_vertices = [False] * number_of_vertices
    vertices_to_visit = [source_vertex]

    while vertices_to_visit:
        current_vertex = vertices_to_visit.pop()
        if current_vertex == destination_vertex:
            return True
        if visited_vertices[current_vertex]:
            continue
        visited_vertices[current_vertex] = True

        for neighbor_vertex in adjacency_list[current_vertex]:
            if not visited_vertices[neighbor_vertex]:
                vertices_to_visit.append(neighbor_vertex)

    return False