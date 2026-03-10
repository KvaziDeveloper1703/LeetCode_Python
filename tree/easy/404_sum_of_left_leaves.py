'''
Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node that has no children. A left leaf is a leaf node that is the left child of its parent node.

Examples:
Input: root = [3, 9, 20, null, null, 15, 7]
Output: 24

Input: root = [1]
Output: 0

Дан корень бинарного дерева root. Необходимо вернуть сумму всех левых листьев.
Лист - это узел, у которого нет дочерних узлов. Левый лист - это лист, который является левым потомком своего родительского узла.

Примеры:
Ввод: root = [3, 9, 20, null, null, 15, 7]
Вывод: 24

Ввод: root = [1]
Вывод: 0
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total = 0
        
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val
        
        total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)
        
        return total