'''
Given the root of a binary tree and an integer target_sum.

Return the number of paths in the tree where the sum of the node values along the path equals target_sum.

The path does not need to start at the root or end at a leaf. However, the path must go downward only — from parent nodes to child nodes.

Examples:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], target_sum = 8
Output: 3

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], target_sum = 22
Output: 3

Дан корень бинарного дерева и целое число target_sum.

Нужно вернуть количество путей в дереве, сумма значений узлов на которых равна target_sum.

Путь не обязан начинаться в корне или заканчиваться в листе. Однако путь должен проходить только вниз — от родителя к потомку.

Примеры:
Ввод: root = [10,5,-3,3,2,null,11,3,-2,null,1], target_sum = 8
Вывод: 3

Ввод: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], target_sum = 22
Вывод: 3
'''

from typing import Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def path_sum(root: Optional[TreeNode], targetSum: int) -> int:

    def dfs(node, current_sum):
        if not node:
            return 0

        current_sum += node.value
        count = prefix_sums[current_sum - targetSum]
        prefix_sums[current_sum] += 1

        count += dfs(node.left, current_sum)
        count += dfs(node.right, current_sum)

        prefix_sums[current_sum] -= 1
        return count

    prefix_sums = defaultdict(int)
    prefix_sums[0] = 1

    return dfs(root, 0)