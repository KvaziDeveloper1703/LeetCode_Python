'''
You are given the root of a binary search tree (BST) that may contain duplicate values.

Your task is to return all mode(s) of the tree - that is, the value(s) that appear most frequently.
    - If there is more than one mode, return all of them in any order.

Definition of a BST:
A binary search tree satisfies the following properties:
    - All values in the left subtree are less than or equal to the node’s value;
    - All values in the right subtree are greater than or equal to the node’s value;
    - Both left and right subtrees are also BSTs.

Examples:
Input: root = [1, null, 2, 2]
Output: [2]

Input: root = [0]
Output: [0]

Дан корень бинарного дерева поиска (BST), которое может содержать повторяющиеся значения.

Ваша задача - найти все моды дерева, то есть значения, которые встречаются наиболее часто.
    - Если мод несколько, верните их в любом порядке.

Определение BST:
Бинарное дерево поиска удовлетворяет следующим условиям:
    - Все значения в левом поддереве меньше или равны значению узла;
    - Все значения в правом поддереве больше или равны значению узла;
    - Левое и правое поддеревья также являются BST.

Примеры:
Ввод: root = [1, null, 2, 2]
Вывод: [2]

Ввод: root = [0]
Вывод: [0]
'''

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        frequency = {}

        def traverse(node):
            if node is None:
                return

            if node.val in frequency:
                frequency[node.val] += 1
            else:
                frequency[node.val] = 1

            traverse(node.left)
            traverse(node.right)

        traverse(root)

        max_count = max(frequency.values())

        result = []

        for value in frequency:
            if frequency[value] == max_count:
                result.append(value)

        return result