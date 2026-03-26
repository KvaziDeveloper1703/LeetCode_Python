'''
You are given the root of a binary tree where each node contains a value of either 0 or 1.
Each path from the root to a leaf represents a binary number, where the root is the most significant bit.

Your task is to:
    - Consider all root-to-leaf paths in the tree;
    - Convert each path into its corresponding binary number;
    - Return the sum of all these numbers.

Дан корень бинарного дерева, где в каждом узле записано значение 0 или 1.
Каждый путь от корня до листа образует двоичное число, при этом корень соответствует старшему разряду.

Что нужно сделать:
    - Рассмотреть все пути от корня до листьев;
    - Преобразовать каждый путь в двоичное число;
    - Вернуть сумму всех полученных чисел.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current):
            if not node:
                return 0

            current = (current << 1) | node.val

            if not node.left and not node.right:
                return current

            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)