'''
You are a great parent and want to give cookies to your children.
Each child can receive at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that makes the child happy.
Each cookie j has a size s[j].
A cookie of size s[j] can be given to a child i if s[j] >= g[i].

Your goal is to maximize the number of content children.
Return the maximum number of children you can make content.

Examples:
Input: g = [1, 2, 3], s = [1, 1]
Output: 1

Input: g = [1, 2], s = [1, 2, 3]
Output: 2

Вы — замечательный родитель и хотите раздать детям печенье.
Каждый ребёнок может получить не более одного печенья.

У каждого ребёнка i есть фактор жадности g[i] — минимальный размер печенья, которое его удовлетворит.
У каждого печенья j есть размер s[j].
Ребёнок будет доволен, если s[j] >= g[i].

Ваша цель — максимизировать количество довольных детей.
Верните максимальное количество детей, которых вы сможете удовлетворить.

Примеры:
Ввод: g = [1, 2, 3], s = [1, 1]
Вывод: 1

Ввод: g = [1, 2], s = [1, 2, 3]
Вывод: 2
'''

from typing import List

def find_content_children(greed_factors: List[int], cookie_sizes: List[int]) -> int:
    greed_factors.sort()
    cookie_sizes.sort()

    child_index = 0
    cookie_index = 0
    number_of_content_children = 0

    while child_index < len(greed_factors) and cookie_index < len(cookie_sizes):
        if cookie_sizes[cookie_index] >= greed_factors[child_index]:
            number_of_content_children += 1
            child_index += 1
        cookie_index += 1

    return number_of_content_children