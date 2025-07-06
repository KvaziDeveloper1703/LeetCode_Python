'''
Given the root of a binary tree and an integer target_sum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals target_sum.
A leaf is a node with no children.

Example:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], target_sum = 22
Output: True

Дано бинарное дерево и целое число target_sum. Нужно вернуть true, если в дереве существует путь от корня до листа, сумма значений вдоль которого равна target_sum.
Лист — это узел, у которого нет дочерних элементов.

Пример:
Ввод: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], target_sum = 22
Вывод: True
'''

from typing import Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False

    if not root.left and not root.right:
        return root.value == target_sum

    remaining_sum = target_sum - root.value
    return (self.has_path_sum(root.left, remaining_sum) or self.has_path_sum(root.right, remaining_sum))