'''
You are given the root of a Binary Search Tree.
Your task is to return the minimum absolute difference between the values of any two different nodes in the tree.

Examples:
Input: root = [4,2,6,1,3]
Output: 1

Input: root = [1,0,48,null,null,12,49]
Output: 1

Дан корень дерева — бинарного дерева поиска.
Найди минимальную абсолютную разницу между значениями любых двух различных узлов в дереве.

Примеры:
Ввод: root = [4,2,6,1,3]
Вывод: 1

Ввод: root = [1,0,48,null,null,12,49]
Вывод: 1
'''

from typing import Optional

class TreeNode:
     def __init__(self, value=0, left=None, right=None):
         self.value = value
         self.left = left
         self.right = right

def get_minimum_difference(root: Optional[TreeNode]) -> int:
    self.previous = None
    self.minimum_difference = float('inf')

    def in_order(node: Optional[TreeNode]):
        if not node:
            return
        in_order(node.left)

        if self.previous is not None:
            self.minimum_difference = min(self.minimum_difference, node.value - self.previous)
        self.previous = node.value

        in_order(node.right)

        in_order(root)
        return self.minimum_difference