'''
You have num_courses courses labeled from 0 to num_courses - 1.
You’re given prerequisites[i] = [a, b] meaning:
to take course a, you must first complete course b.

Return true if it’s possible to finish all courses.
Otherwise, return false.

Example:
Input:
num_courses = 2
prerequisites = [[1, 0]]

Output:
true

У тебя есть num_courses курсов, пронумерованных от 0 до num_courses - 1.
Дан список prerequisites, где prerequisites[i] = [a, b] означает:
чтобы взять курс a, нужно сначала пройти курс b.

Нужно вернуть true, если все курсы можно пройти.
Иначе вернуть false.

Пример:
Ввод:
num_courses = 2
prerequisites = [[1, 0]]

Вывод:
true
'''

from typing import List
from collections import defaultdict

class Solution:
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(List)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = [0] * num_courses

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

        for course in range(num_courses):
            if has_cycle(course):
                return False

        return True