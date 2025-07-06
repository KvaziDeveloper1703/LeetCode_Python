'''
Given the roots of two binary trees p and q, write a function to determine whether the two trees are identical.
Two binary trees are considered the same if they have the same structure, and all corresponding nodes have the same values.

Examples:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Даны корни двух бинарных деревьев p и q. Напишите функцию, которая определяет, являются ли эти деревья одинаковыми.
Два бинарных дерева считаются одинаковыми, если они имеют одинаковую структуру, и значения всех соответствующих узлов в них совпадают.

Примеры:
Ввод: p = [1,2,3], q = [1,2,3]
Вывод: true

Ввод: p = [1,2], q = [1,null,2]
Вывод: false
'''

from typing import Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.value != q.value:
            return False

        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)