'''
You are given the root of a binary search tree and an integer k.
Your task is to determine whether there are two different nodes in the tree whose values add up to k.
Return true if such a pair exists. Otherwise, return false

Дан корень бинарного дерева поиска и целое число k.
Необходимо определить, существуют ли две разные вершины дерева, сумма значений которых равна k.
Верните true, если такая пара есть. Иначе верните false
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        def dfs(node):
            if not node:
                return False

            if k - node.val in seen:
                return True

            seen.add(node.val)

            return dfs(node.left) or dfs(node.right)

        return dfs(root)