'''
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
A leaf is a node with no children.

Examples:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Дано бинарное дерево. Найдите его минимальную глубину.
Минимальная глубина — это количество узлов на самом коротком пути от корневого узла до ближайшего листового узла.
Лист — это узел, у которого нет потомков.

Примеры:
Ввод: root = [3,9,20,null,null,15,7]
Вывод: 2

Ввод: root = [2,null,3,null,4,null,5,null,6]
Вывод: 5
'''

from typing import Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def minimum_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    if not root.left:
        return self.minimum_depth(root.right) + 1
    if not root.right:
        return self.minimum_depth(root.left) + 1
    return min(self.minimum_depth(root.left), self.minimum_depth(root.right)) + 1