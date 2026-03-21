'''
You are given the root of a binary search tree and an integer val.
Your task is to find the node in the tree whose value is equal to val.
If such a node exists, return the subtree rooted at that node. If no such node exists, return null.

Дан корень бинарного дерева поиска и целое число val.
Необходимо найти вершину дерева, значение которой равно val.
Если такая вершина найдена, вернуть поддерево с корнем в этой вершин. Если такой вершины нет, вернуть null.
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root

        while current:
            if current.val == val:
                return current
            elif val < current.val:
                current = current.left
            else:
                current = current.right

        return None