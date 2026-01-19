'''
Given the root of a binary tree, return the preorder traversal of its nodes values.

In preorder traversal, the nodes are visited in this order:
    - Root;
    - Left subtree;
    - Right subtree.

Examples:
Input: root = [1, null, 2, 3]
Output: [1, 2, 3]

Input: root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]
Output: [1, 2, 4, 5, 6, 7, 3, 8, 9]

Дан корень бинарного дерева. Верни значения его узлов в порядке обхода в глубину Preorder.

В Preorder обход выполняется в следующем порядке:
    - Корень;
    - Левое поддерево;
    - Правое поддерево.

Примеры:
Ввод: root = [1, null, 2, 3]
Вывод: [1, 2, 3]

Ввод: root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]
Вывод: [1, 2, 4, 5, 6, 7, 3, 8, 9]
'''

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.value)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result