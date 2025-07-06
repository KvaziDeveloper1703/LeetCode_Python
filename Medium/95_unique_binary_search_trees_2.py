'''
You are given an integer n. Your task is to return all structurally unique Binary Search Trees (BSTs) that store values from 1 to n.
Each tree must have exactly n nodes, and each node must have a unique value from 1 to n.
Return the list of all possible BSTs in any order.

Example:
Input: n = 3
Output: [[1,null,2,null,3], [1,null,3,2], [2,1,3], [3,1,null,null,2], [3,2,null,1]]

Дано целое число n. Необходимо вернуть все структурно уникальные бинарные деревья поиска (BST), которые можно построить, используя значения от 1 до n.
Каждое дерево должно содержать ровно n узлов, и значения в них должны быть уникальными — от 1 до n.
Вернуть нужно список всех возможных деревьев в любом порядке.

Пример:
Ввод: n = 3
Вывод: [[1,null,2,null,3], [1,null,3,2], [2,1,3], [3,1,null,null,2], [3,2,null,1]]
'''

from typing import List, Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def build_trees(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]

            all_trees = []

            for root_value in range(start, end + 1):
                left_trees = build_trees(start, root_value - 1)
                right_trees = build_trees(root_value + 1, end)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_value)
                        root.left = left
                        root.right = right
                        all_trees.append(root)

            return all_trees

        return build_trees(1, n)