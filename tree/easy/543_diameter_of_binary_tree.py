'''
You are given the root of a binary tree. Your task is to return the diameter of the tree.
The diameter of a binary tree is defined as the length of the longest path between any two nodes in the tree.
    - This path may or may not pass through the root;
    - The length of the path is measured as the number of edges between the two nodes.

Examples:
Input: root = [1, 2, 3, 4, 5]
Output: 3

Input: root = [1, 2]
Output: 1

Дан корень бинарного дерева. Ваша задача - найти диаметр дерева.
Диаметр бинарного дерева - это длина самого длинного пути между любыми двумя узлами дерева.
    - Этот путь может проходить через корень, а может и не проходить;
    - Длина пути определяется как количество рёбер между двумя узлами.

Примеры:
Ввод: root = [1, 2, 3, 4, 5]
Вывод: 3

Ввод: root = [1, 2]
Вывод: 1
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def depth(node):
            nonlocal max_diameter

            if node is None:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            current_diameter = left_depth + right_depth

            if current_diameter > max_diameter:
                max_diameter = current_diameter

            return max(left_depth, right_depth) + 1

        depth(root)

        return max_diameter