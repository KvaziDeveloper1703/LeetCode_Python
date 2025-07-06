'''
You are given the root of a binary tree. Your task is to return the inorder traversal of the tree's node values.

Inorder traversal means:
    + Visit the left subtree;
    + Then visit the current node;
    + Then visit the right subtree.

Return a list of integers representing the values of the nodes in inorder.

Examples:
Input: root = [1, null, 2, 3]
Output: [1, 3, 2]

Input: root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]
Output: [4, 2, 6, 5, 7, 1, 3, 9, 8]

Дан корень бинарного дерева root. Нужно вернуть содержимое узлов дерева в порядке симметричного обхода (inorder traversal).

Симметричный обход — это:
+ Сначала обход левого поддерева;
+ Затем текущий узел;
+ Затем обход правого поддерева.

Необходимо вернуть cписок значений узлов в порядке симметричного обхода.

Примеры:
Ввод: root = [1, null, 2, 3]
Вывод: [1, 3, 2]

Ввод: root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]
Вывод: [4, 2, 6, 5, 7, 1, 3, 9, 8]
'''

from typing import Optional, List

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node: Optional[TreeNode]):
            if node:
                inorder(node.left)
                result.append(node.value)
                inorder(node.right)

        inorder(root)
        return result