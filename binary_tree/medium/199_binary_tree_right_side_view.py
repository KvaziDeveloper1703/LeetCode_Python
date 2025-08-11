'''
Given the root of a binary tree, imagine yourself standing on the right side of it.

Return the values of the nodes you can see, from top to bottom, one per level.

Example:
Input: root = [1,2,3,null,5,null,4]
Output: [1, 3, 4]

Дано бинарное дерево. Представь, что ты смотришь на него справа.

Верни список значений узлов, которые ты видишь с правой стороны, сверху вниз, по одному узлу на каждый уровень дерева.

Пример:
Ввод: root = [1,2,3,null,5,null,4]
Вывод: [1, 3, 4]
'''

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def right_side_view(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_length = len(queue)

        for i in range(level_length):
            current_node = queue.popleft()

            if i == level_length - 1:
                result.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    return result