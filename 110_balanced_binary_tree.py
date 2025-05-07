'''
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example:
Input: root = [3,9,20,null,null,15,7]
Output: true

Дано бинарное дерево. Определите, является ли оно сбалансированным по высоте.
Сбалансированное по высоте дерево — это такое бинарное дерево, в котором глубина двух поддеревьев любого узла отличается не более чем на один.

Пример:
Ввод: root = [3,9,20,null,null,15,7]
Вывод: true
'''

from typing import Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            if left == -1:
                return -1
            right = check(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return check(root) != -1