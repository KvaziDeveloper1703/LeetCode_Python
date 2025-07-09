'''
You have number_of_courses courses labeled from 0 to number_of_courses - 1.
You’re given prerequisites[i] = [a, b] meaning: to take course a, you must first complete course b.

Return True if it’s possible to finish all courses. Otherwise, return False.

Example:
Input: number_of_courses = 2, prerequisites = [[1, 0]]
Output: True

У тебя есть number_of_courses курсов, пронумерованных от 0 до number_of_courses - 1.
Дан список prerequisites, где prerequisites[i] = [a, b] означает: чтобы взять курс a, нужно сначала пройти курс b.

Нужно вернуть True, если все курсы можно пройти. Иначе вернуть False.

Пример:
Ввод: number_of_courses = 2, prerequisites = [[1, 0]]
Вывод: True
'''

from typing import List
from collections import defaultdict

def can_finish(number_of_courses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(List)

    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)

    visited = [0] * number_of_courses

    def has_cycle(course: int) -> bool:
        if visited[course] == 1:
            return True
        if visited[course] == 2:
            return False

        visited[course] = 1
        for neighbor in graph[course]:
            if has_cycle(neighbor):
                return True

            visited[course] = 2
            return False

        for course in range(number_of_courses):
            if has_cycle(course):
                return False

        return True