'''
Given the root of a binary tree, check whether it is a mirror of itself, is it symmetric around its center.

Example:
Input: root = [1,2,2,3,4,4,3]
Output: true

Дано корневое значение бинарного дерева. Необходимо проверить, является ли дерево зеркальным отображением самого себя то есть симметричным относительно своего центра.

Пример:
Ввод: root = [1,2,2,3,4,4,3]
Вывод: true
'''

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, value=0, left_child=None, right_child=None):
        self.value = value
        self.left = left_child
        self.right = right_child

class Solution:
    def is_symmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(subtree_left: TreeNode, subtree_right: TreeNode) -> bool:
            if not subtree_left and not subtree_right:
                return True
            if not subtree_left or not subtree_right:
                return False
            return (
                subtree_left.value == subtree_right.value and
                is_mirror(subtree_left.left, subtree_right.right) and
                is_mirror(subtree_left.right, subtree_right.left)
            )

        return is_mirror(root, root)

    def is_symmetric_iterative(self, root: Optional[TreeNode]) -> bool:
        node_queue = deque([(root, root)])
        while node_queue:
            left_node, right_node = node_queue.popleft()
            
            if not left_node and not right_node:
                continue
            if not left_node or not right_node:
                return False
            if left_node.value != right_node.value:
                return False
            
            node_queue.append((left_node.left, right_node.right))
            node_queue.append((left_node.right, right_node.left))
        
        return True