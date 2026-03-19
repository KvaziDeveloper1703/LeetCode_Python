'''
You are given the roots of two binary trees: root and subRoot.
Your task is to determine whether subRoot is a subtree of root.

Definition:
A subtree of a binary tree is a tree consisting of:
    - a node in the original tree, and
    - all of its descendants.

The tree root itself can also be considered a subtree of itself.

Conditions:
    - The subtree must have the same structure as subRoot;
    - All corresponding nodes must have the same values.

Return true if there exists a subtree in root that is identical to subRoot, and false otherwise.

Даны корни двух бинарных деревьев: root и subRoot.
Необходимо определить, является ли subRoot поддеревом дерева root.

Определение:
Поддерево бинарного дерева - это дерево, которое состоит из:
    - некоторого узла исходного дерева, и
    - всех его потомков.

При этом само дерево root также считается своим поддеревом.

Условия:
    - Поддерево должно иметь такую же структуру, как subRoot;
    - Все соответствующие узлы должны иметь одинаковые значения.

Вернуть true, если в root существует поддерево, совпадающее с subRoot, и false в противном случае.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root, subRoot):
        def isSameTree(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False

            return (isSameTree(a.left, b.left) and 
                    isSameTree(a.right, b.right))

        def dfs(node):
            if not node:
                return False

            if isSameTree(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)

        return dfs(root)