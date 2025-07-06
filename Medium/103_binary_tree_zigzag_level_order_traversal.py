'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values:
+ First level: left to right;
+ Second level: right to left;
+ Third level: left to right.

Alternate directions at each level

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Дано бинарное дерево. Требуется вернуть зигзагообразный уровневой обход значений его узлов:
+ Первый уровень — слева направо;
+ Второй уровень — справа налево;
+ Третий — снова слева направо.

И так далее, чередуя направление на каждом уровне

Пример:
Ввод:root = [3,9,20,null,null,15,7]
Вывод: [[3],[20,9],[15,7]]
'''

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def zigzag_level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            current_level = deque()

            for _ in range(level_size):
                node = queue.popleft()

                if left_to_right:
                    current_level.append(node.value)
                else:
                    current_level.appendleft(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(list(current_level))
            left_to_right = not left_to_right

        return result