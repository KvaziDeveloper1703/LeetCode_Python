'''
You are given the root of a binary tree with unique values, and two values x and y corresponding to two different nodes in the tree.

Two nodes are called cousins if:
    - They are at the same depth, and
    - They have different parents.

Notes:
    - The root node has depth 0;
    - If a node has depth k, then its children have depth k + 1.

Return true if the nodes with values x and y are cousins, otherwise return false.

Дан корень бинарного дерева с уникальными значениями, а также значения двух различных узлов x и y.

Два узла называются двоюродными, если:
    - Они находятся на одной глубине, и
    - У них разные родители.

Примечания:
    - Корень дерева имеет глубину 0;
    - Если узел находится на глубине k, то его дети находятся на глубине k + 1.

Вернуть true, если узлы со значениями x и y являются двоюродными, и false в противном случае.
'''

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:        
        queue = deque([(root, None)])

        while queue:
            level_size = len(queue)
            x_parent = None
            y_parent = None

            for _ in range(level_size):
                node, parent = queue.popleft()

                if node.val == x:
                    x_parent = parent
                if node.val == y:
                    y_parent = parent

                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))

            if x_parent and y_parent:
                return x_parent != y_parent

            if x_parent or y_parent:
                return False

        return False