'''
Given an integer array numbers where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
A height-balanced BST is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example:
Input: numbers = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]

Дан целочисленный массив numbers, элементы которого отсортированы по возрастанию. Преобразуйте его в сбалансированное бинарное дерево поиска.
Сбалансированное по высоте дерево — это такое бинарное дерево, в котором глубина двух поддеревьев любого узла отличается не более чем на один.

Пример:
Ввод: numbers = [-10,-3,0,5,9]
Вывод: [0,-3,9,-10,null,5]
'''

from typing import List, Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, numbers: List[int]) -> Optional[TreeNode]:
        if not numbers:
            return None

        mid = len(numbers) // 2
        root = TreeNode(numbers[mid])
        
        root.left = self.sortedArrayToBST(numbers[:mid])
        root.right = self.sortedArrayToBST(numbers[mid+1:])
        
        return root