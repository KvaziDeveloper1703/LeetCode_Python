'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes p and q.
According to the definition on Wikipedia: The lowest common ancestor is defined between two nodes p and q as the lowest node T in the tree that has both p and q as descendants.

Example:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3

Дано бинарное дерево и два узла p и q.
Найди наименьшего общего предка (Lowest Common Ancestor, LCA) этих двух узлов.

Согласно определению из Википедии: Наименьший общий предок (Lowest Common Ancestor) двух узлов p и q — это самый низкий (глубокий) узел T в дереве, такой, что оба узла p и q являются потомками T.

Пример:
Ввод: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Выход: 3
'''

from typing import Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def lowest_common_ancestor(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        if not root or root == p or root == q:
            return root
        
        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right