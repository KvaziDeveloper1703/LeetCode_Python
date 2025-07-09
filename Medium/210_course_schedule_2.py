''' 
You are given number_of_courses labeled from 0 to nummber_of_courses - 1, and an array prerequisites where prerequisites[i] = [a, b] means: to take course a, you must first complete course b.

Return a valid order to complete all courses.
    + If multiple valid orders exist, return any of them.
    + If it's impossible to finish all courses, return an empty array.

Example:
Input: number_of_courses = 2, prerequisites = [[1, 0]]
Output: [0, 1]

Дано количество курсов number_of_courses (нумеруются от 0 до number_of_courses - 1) и список prerequisites, где prerequisites[i] = [a, b] означает: чтобы взять курс a, нужно сначала пройти курс b.

Требуется вернуть один из возможных порядков прохождения всех курсов так, чтобы были выполнены все зависимости. Если пройти все курсы невозможно, вернуть пустой список.

Пример:
Ввод: number_of_courses = 2, prerequisites = [[1, 0]]
Вывод: [0, 1]
'''

from typing import List
from collections import defaultdict, deque

def find_order(number_of_courses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = defaultdict(list)
    in_degree = [0] * number_of_courses

    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        in_degree[course] += 1

    queue = deque([i for i in range(number_of_courses) if in_degree[i] == 0])
    order = []

    while queue:
        current = queue.popleft()
        order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == number_of_courses else []