'''
You are given the roots of two binary trees: root1 and root2.

Imagine placing one tree on top of the other. In this case:
    - Some nodes overlap,
    - Some nodes exist in only one of the trees.

Your task is to merge the two trees into a new binary tree.

Merge rules:
    - If two nodes overlap, their values are summed, and the result becomes the value of the new node;
    - If only one node exists, use the non-null node in the new tree.

Important:
    - The merging process starts from the root nodes of both trees;
    - The process continues recursively for all child nodes.

Return the root of the merged binary tree.

Даны корни двух бинарных деревьев: root1 и root2.

Представьте, что одно дерево накладывается на другое:
    - Некоторые узлы совпадают по позиции,
    - Некоторые существуют только в одном из деревьев.

Необходимо объединить эти два дерева в новое бинарное дерево.

Правила объединения:
    - Если узлы перекрываются, их значения складываются, и сумма становится значением нового узла;
    - Если существует только один узел (второй равен null), используется ненулевой узел.

Важно:
    - Объединение начинается с корневых узлов обоих деревьев;
    - Далее процесс выполняется рекурсивно для всех потомков.

Вернуть корень нового объединённого дерева.
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        root1.val += root2.val

        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1