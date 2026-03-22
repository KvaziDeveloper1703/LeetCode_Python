'''
You are given the root of a binary search tree.

Rearrange the tree so that it becomes an in-order increasing tree, where:
    - The leftmost node of the original tree becomes the new root;
    - Every node has no left child;
    - Each node has only one right child;
    - The nodes are arranged in the same order as an in-order traversal of the original tree.

In other words, you should transform the BST into a tree that looks like a right-skewed linked list, following the in-order sequence.
Return the root of the rearranged tree.

Дан корень бинарного дерева поиска.

Необходимо преобразовать дерево так, чтобы:
- Самый левый узел стал новым корнем;
- У каждого узла не было левого потомка;
- У каждого узла был только один правый потомок;
- Узлы располагались в порядке in-order обхода исходного дерева.

Другими словами, нужно превратить дерево в структуру, похожую на односвязный список вправо, сохраняя порядок in-order.
Вернуть корень преобразованного дерева.
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        dummy = TreeNode(0)
        current = dummy

        def inorder(node):
            nonlocal current

            if not node:
                return

            inorder(node.left)

            node.left = None
            current.right = node
            current = node

            inorder(node.right)

        inorder(root)

        return dummy.right