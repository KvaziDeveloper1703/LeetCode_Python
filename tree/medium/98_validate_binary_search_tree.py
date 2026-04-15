'''
You are given the root of a binary tree. Determine whether it is a valid Binary Search Tree.

A binary tree is a valid BST if:
    + The left subtree of a node contains only nodes with values less than the node’s value;
    + The right subtree of a node contains only nodes with values greater than the node’s value;
    + Both subtrees must also be valid BSTs.

Examples:
Input: root = [2,1,3]
Output: True

Input: root = [5,1,4,null,null,3,6]
Output: False

Дан корень бинарного дерева. Определи, является ли оно корректным бинарным деревом поиска.

Бинарное дерево считается корректным BST, если выполняются условия:
    + В левом поддереве узла находятся только значения меньше значения самого узла;
    + В правом поддереве узла — только значения больше;
    + Оба поддерева также должны быть корректными BST.

Примеры:
Ввод: root = [2,1,3]
Вывод: True

Ввод: root = [5,1,4,null,null,3,6]
Вывод: False
'''

from typing import Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_valid_BST(root: Optional[TreeNode]) -> bool:
    def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
        if not node:
            return True

        if not (low < node.value < high):
            return False
        return (
            validate(node.left, low, node.value) and
            validate(node.right, node.value, high)
        )

    return validate(root, float('-inf'), float('inf'))