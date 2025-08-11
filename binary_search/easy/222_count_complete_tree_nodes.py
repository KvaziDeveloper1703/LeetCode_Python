'''
Given the root of a complete binary tree, return the number of nodes in the tree.
According to Wikipedia, a complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
The last level h can contain between 1 and 2^h nodes.

Дан корень полного бинарного дерева. Требуется вернуть количество узлов в этом дереве.
Согласно Википедии, полное бинарное дерево — это дерево, у которого все уровни, кроме, возможно, последнего, полностью заполнены, а все узлы на последнем уровне находятся максимально слева.
Последний уровень дерева (глубина h) может содержать от 1 до 2^h узлов.
'''

from typing import Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def count_nodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def get_depth(node: Optional[TreeNode], go_left: bool) -> int:
            depth = 0
            while node:
                depth += 1
                node = node.left if go_left else node.right
            return depth

        left_depth = get_depth(root, True)
        right_depth = get_depth(root, False)

        if left_depth == right_depth:
            return (1 << left_depth) - 1
        else:
            return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)