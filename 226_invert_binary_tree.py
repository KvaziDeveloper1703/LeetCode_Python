'''
Given the root of a binary tree, invert the tree and return its root.
Inverting a binary tree means swapping the left and right children of every node in the tree.

Examples:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Input: root = [2,1,3]
Output: [2,3,1]

Дан корень бинарного дерева root. Инвертируйте дерево и верните его корень.
Инвертировать бинарное дерево — значит поменять местами левого и правого потомков каждого узла дерева.

Примеры:
Ввод: root = [4,2,7,1,3,6,9]
Вывод: [4,7,2,9,6,3,1]

Ввод: root = [2,1,3]
Вывод: [2,3,1]
'''

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root