'''
You are given a non-empty special binary tree where:
    - Each node contains a non-negative integer;
    - Every node has either exactly two children or no children;
    - If a node has two children, its value is equal to the minimum of its children’s values.

Your task is to find the second smallest value among all values in the tree.
Return the second minimum value if it exists. Otherwise, return -1 if all values in the tree are the same.

Дано непустое специальное бинарное дерево, в котором:
    - Каждая вершина содержит неотрицательное целое число;
    - У каждой вершины либо ровно два потомка, либо нет потомков;
    - Если у вершины есть два потомка, её значение равно минимуму из значений её детей.

Необходимо найти второе по величине минимальное значение среди всех значений в дереве.
Верните это значение, если оно существует. Если все значения одинаковые, верните -1.
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        min_val = root.val
        self.second_min = float('inf')

        def dfs(node):
            if not node:
                return

            if min_val < node.val < self.second_min:
                self.second_min = node.val

            elif node.val == min_val:
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        return self.second_min if self.second_min != float('inf') else -1