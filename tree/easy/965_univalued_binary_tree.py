'''
A binary tree is called uni-valued if all of its nodes have the same value.
You are given the root of a binary tree.
Return true if the tree is uni-valued, otherwise return false.

Бинарное дерево называется uni-valued, если все его узлы имеют одинаковое значение.
Дан корень бинарного дерева.
Вернуть true, если дерево является однородным, и false в противном случае.
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, value):
            if not node:
                return True

            if node.val != value:
                return False

            return dfs(node.left, value) and dfs(node.right, value)

        return dfs(root, root.val)