'''
You are given the root of a binary search tree and two integers low and high.
Find the sum of all node values such that each value lies within the inclusive range [low, high].

Important notes:
    - Only include nodes where low ≤ node.val ≤ high;
    - The tree follows BST properties:
        - Left subtree contains smaller values;
        - Right subtree contains larger values.

Return the sum of all values within the given range.

Дан корень бинарного дерева поиска и два числа low и high.
Необходимо найти сумму значений всех узлов, значения которых находятся в включительном диапазоне [low, high].

Важно:
    - Учитываются только те узлы, для которых выполняется: low ≤ значение узла ≤ high;
    - Дерево является BST:
        - В левом поддереве значения меньше;
        - В правом - больше.

Вернуть сумму всех значений узлов в заданном диапазоне.
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        return (
            root.val +
            self.rangeSumBST(root.left, low, high) +
            self.rangeSumBST(root.right, low, high)
        )