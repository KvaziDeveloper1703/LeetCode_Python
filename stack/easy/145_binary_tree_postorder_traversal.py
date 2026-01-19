'''
Given the root of a binary tree, return the postorder traversal of its nodes values.

In postorder traversal, the nodes are visited in this order:
    - Left subtree;
    - Right subtree;
    - Root.

Examples:
Input: root = [1, null, 2, 3]
Output: [3, 2, 1]

Input: root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]
Output: [4, 6, 7, 5, 2, 9, 8, 3, 1]

Дан корень бинарного дерева. Верни значения узлов при обходе Postorder.

В Postorder узлы посещаются в следующем порядке:
    - Левое поддерево;
    - Правое поддерево;
    - Корень.

Примеры:
Ввод: root = [1, null, 2, 3]
Вывод: [3, 2, 1]

Ввод: root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]
Вывод: [4, 6, 7, 5, 2, 9, 8, 3, 1]
'''

from typing import Optional, List

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            if visited:
                result.append(node.value)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return result