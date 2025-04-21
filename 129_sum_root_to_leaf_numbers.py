'''
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
For example, the path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers.
A leaf node is a node with no children.

Example:
Input: root = [1,2,3]
Output: 25

Дано бинарное дерево, в каждом узле которого содержится одна цифра от 0 до 9.
Каждый путь от корня до листа дерева представляет собой число, составленное из цифр вдоль этого пути.
Например, путь 1 → 2 → 3 представляет число 123.

Нужно вернуть сумму всех таких чисел, образованных от корня до каждого листа.
Лист — это узел, у которого нет детей.

Пример:
Ввод: root = [1,2,3]
Вывод: 25
'''

from typing import Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def sum_numbers(self, root: Optional[TreeNode]) -> int:
        def dfs(current_node: TreeNode, current_number: int) -> int:
            if not current_node:
                return 0

            current_number = current_number * 10 + current_node.value

            if not current_node.left and not current_node.right:
                return current_number

            return dfs(current_node.left, current_number) + dfs(current_node.right, current_number)

        return dfs(root, 0)