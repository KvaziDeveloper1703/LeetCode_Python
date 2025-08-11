'''
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.

Examples:
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

Input: root = [1]
Output: [[1]]

Дан корень бинарного дерева. Верните обход по уровням снизу вверх, то есть список значений узлов, начиная с листьев к корню, проходя уровень за уровнем слева направо.

Примеры:
Ввод: root = [3,9,20,null,null,15,7]
Вывод: [[15,7],[9,20],[3]]

Ввод: root = [1]
Вывод: [[1]]
'''

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_order_bottom(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result[::-1]