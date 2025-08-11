'''
Given the root of a binary search tree and an integer k.

Return the k-th smallest value in the tree (using 1-based indexing).

Examples:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Дан корень бинарного дерева поиска и целое число k.

Найди k-ое наименьшее значение в дереве (нумерация с 1).

Примеры:
Ввод: root = [3,1,4,null,2], k = 1
Вывод: 1

Ввод: root = [5,3,6,2,4,null,null,1], k = 3
Вывод: 3
'''

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

from typing import Optional

def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    self.count = 0
    self.result = None

    def in_order(node: Optional[TreeNode]):
        if not node or self.result is not None:
            return
        in_order(node.left)

        self.count += 1
        if self.count == k:
            self.result = node.val
            return

        in_order(node.right)

    in_order(root)
    return self.result