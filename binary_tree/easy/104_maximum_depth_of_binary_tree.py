'''
You are given the root of a binary tree, return the maximum depth of the tree.
The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the deepest leaf node.

Examples:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2

Дан корень бинарного дерева root. Верните максимальную глубину дерева.
Максимальная глубина бинарного дерева — это количество узлов вдоль самого длинного пути от корневого узла до самого глубоко расположенного листового узла.

Примеры:
Ввод: root = [3,9,20,null,null,15,7]
Вывод: 3

Ввод: root = [1,null,2]
Вывод: 2
'''

from typing import Optional

class TreeNode:
     def __init__(self, value=0, left=None, right=None):
         self.value = value
         self.left = left
         self.right = right

def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(self.max_depth(root.left), self.max_depth(root.right))