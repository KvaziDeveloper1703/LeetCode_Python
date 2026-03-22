'''
You are given two binary trees with root nodes root1 and root2.
Consider all the leaf nodes of each tree. If you list the values of these leaf nodes from left to right, you obtain a leaf value sequence.
Two binary trees are called leaf-similar if their leaf value sequences are exactly the same.
Return true if the two given trees are leaf-similar, and false otherwise.

Даны два бинарных дерева с корнями root1 и root2.
Рассмотрим все листовые вершины каждого дерева. Если выписать значения этих листьев слева направо, получится последовательность значений листьев.
Два бинарных дерева называются leaf-similar, если их последовательности значений листьев полностью совпадают.
Вернуть true, если деревья являются leaf-similar, и false в противном случае.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def get_leaves(root: Optional[TreeNode]) -> List[int]:
            leaves = []

            def dfs(node):
                if not node:
                    return

                if not node.left and not node.right:
                    leaves.append(node.val)
                    return

                dfs(node.left)
                dfs(node.right)

            dfs(root)
            return leaves

        return get_leaves(root1) == get_leaves(root2)