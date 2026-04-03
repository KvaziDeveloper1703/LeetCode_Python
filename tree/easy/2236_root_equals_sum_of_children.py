'''
You are given the root of a binary tree that consists of exactly three nodes: the root, its left child, and its right child.
Return true if the value of the root is equal to the sum of the values of its two children, otherwise return false.

Examples:
Input: root = [10, 4, 6]
Output: true

Input: root = [5, 3, 1]
Output: false

Дан корень бинарного дерева, состоящего ровно из трёх узлов: корня, его левого и правого потомков.
Необходимо вернуть true, если значение корня равно сумме значений двух его потомков, иначе вернуть false.

Примеры:
Ввод: root = [10, 4, 6]
Вывод: true

Ввод: root = [5, 3, 1]
Вывод: false
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkTree(self, root) -> bool:
        left_value = root.left.val
        right_value = root.right.val
        return root.val == left_value + right_value