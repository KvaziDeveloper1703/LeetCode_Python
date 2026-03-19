'''
You are given the root of a binary tree. Your task is to return the sum of the tilt of all nodes in the tree.

Definition:
The tilt of a node is defined as the absolute difference between:
    - the sum of all values in its left subtree, and
    - the sum of all values in its right subtree.

Notes:
    - If a node has no left child, the sum of the left subtree is considered 0;
    - If a node has no right child, the sum of the right subtree is considered 0.

Compute the tilt for every node and return the total sum of all tilts.

Дан корень бинарного дерева. Необходимо найти сумму наклонов (tilt) всех узлов дерева.

Определение:
Наклон узла - это модуль разности между:
    - суммой значений всех узлов в левом поддереве, и
    - суммой значений всех узлов в правом поддереве.

Примечания:
    - Если у узла нет левого потомка, сумма левого поддерева считается равной 0;
    - Если у узла нет правого потомка, сумма правого поддерева считается равной 0.

Нужно вычислить наклон каждого узла и вернуть сумму всех наклонов в дереве.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root):
        self.total_tilt = 0

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            self.total_tilt += abs(left_sum - right_sum)

            return left_sum + right_sum + node.val

        dfs(root)
        return self.total_tilt