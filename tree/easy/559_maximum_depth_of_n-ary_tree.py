'''
You are given the root of an n-ary tree. Your task is to find its maximum depth.
The maximum depth is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

Input format:
The tree is given using level-order traversal.
    - Each group of children is separated by a null value;
    - This representation helps indicate which nodes belong to the same parent.

Examples:
Input: root = [1, null, 3, 2, 4, null, 5, 6]
Output: 3

Input: root = [1, null, 2, 3, 4, 5, null, null, 6, 7, null, 8, null, 9, 10, null, null, 11, null, 12, null, 13, null, null, 14]
Output: 5

Дан корень n-арного дерева. Ваша задача - найти его максимальную глубину.
Максимальная глубина - это количество узлов на самом длинном пути от корня до самого удалённого листа.

Формат входных данных:
Дерево задано в виде обхода в ширину.
    - Каждая группа дочерних узлов разделяется значением null;
    - Это позволяет определить, какие узлы являются детьми одного родителя.

Примеры:
Ввод: root = [1, null, 3, 2, 4, null, 5, 6]
Вывод: 3

Ввод: root = [1, null, 2, 3, 4, 5, null, null, 6, 7, null, 8, null, 9, 10, null, null, 11, null, 12, null, 13, null, null, 14]
Вывод: 5
'''

from typing import List, Optional

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: Optional['Node']) -> int:
        if root is None:
            return 0

        max_child_depth = 0

        for child in root.children:
            child_depth = self.maxDepth(child)

            if child_depth > max_child_depth:
                max_child_depth = child_depth

        return max_child_depth + 1