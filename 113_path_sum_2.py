'''
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
+ Each path should be returned as a list of the node values, not node references.
+ A root-to-leaf path is a path starting from the root and ending at any leaf node.
+ A leaf is a node with no children.

Example:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

Дано бинарное дерево с корнем root и целое число targetSum. Верните все пути от корня до листьев, сумма значений узлов в которых равна targetSum.
+ Каждый путь должен быть представлен списком значений узлов, а не ссылками на узлы.
+ Путь от корня до листа — это путь, начинающийся в корне и заканчивающийся в листовом узле.
+ Лист — это узел без потомков.

Пример:
Ввод: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Вывод: [[5,4,11,2],[5,8,4,5]]
'''

from typing import Optional, List

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, path, current_sum):
            if not node:
                return

            path.append(node.value)
            current_sum += node.value

            if not node.left and not node.right and current_sum == targetSum:
                result.append(list(path))

            dfs(node.left, path, current_sum)
            dfs(node.right, path, current_sum)
            path.pop()

        dfs(root, [], 0)
        return result