'''
You are given the root of a binary search tree.
Your task is to find the minimum absolute difference between the values of any two different nodes in the tree.
Return this minimum difference.

Дан корень бинарного дерева поиска.
Необходимо найти минимальную разницу по модулю между значениями любых двух разных вершин дерева.
Верните это минимальное значение.
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)

            self.prev = node.val

            inorder(node.right)

        inorder(root)
        return self.min_diff