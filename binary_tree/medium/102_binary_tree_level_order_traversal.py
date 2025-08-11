'''
Given the root of a binary tree.

Return the level order traversal of its nodes' values.

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Дано бинарное дерево. 

Требуется вернуть уровневой обход его узлов — то есть, список списков значений узлов, слева направо, уровень за уровнем.

Пример:
Ввод: root = [3,9,20,null,null,15,7]
Вывод: [[3],[9,20],[15,7]]
'''

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        result.append(current_level)

    return result