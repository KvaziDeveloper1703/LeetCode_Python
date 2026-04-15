'''
You are given the root of a binary search tree, where the values of exactly two nodes were swapped by mistake.
Your task is to recover the tree without changing its structure.

Examples:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]

Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]

Дан корень бинарного дерева поиска, в котором значения ровно двух узлов были по ошибке перепутаны.
Необходимо восстановить дерево, не изменяя его структуру.

Примеры:
Ввод: root = [1,3,null,null,2]
Вывод: [3,1,null,null,2]

Ввод: root = [3,1,4,null,null,2]
Вывод: [2,1,4,null,null,3]
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node

            self.prev = node

            inorder(node.right)

        inorder(root)

        self.first.val, self.second.val = self.second.val, self.first.val