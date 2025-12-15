'''
You are given the root of a full binary tree with the following properties:
    - Leaf nodes have a value of either 0 or 1, where:
        - 0 represents False;
        - 1 represents True.
    - Non-leaf nodes have a value of either 2 or 3, where:
        - 2 represents the boolean OR operation;
        - 3 represents the boolean AND operation.

The evaluation of a node is defined as follows:
    - If the node is a leaf node, its evaluation is simply its value.
    - Otherwise, first evaluate the node’s two children, then apply the boolean operation specified by the node’s value to the children’s results.

Return the boolean result of evaluating the root node.

A full binary tree is a binary tree in which every node has either 0 or 2 children.
A leaf node is a node that has no children.

Examples:
Input: root = [2, 1, 3, null, null, 0, 1]
Output: True

Input: root = [0]
Output: False

Дан корень полного бинарного дерева со следующими свойствами:
    - Листовые узлы имеют значение 0 или 1, где:
        - 0 означает False;
        - 1 означает True.
    - Нелистовые узлы имеют значение 2 или 3, где:
        - 2 обозначает логическую операцию OR;
        - 3 обозначает логическую операцию AND.
    - Правила вычисления значения узла:
        - Если узел является листовым, его значение равно значению узла.
        - В противном случае сначала вычисляются значения двух дочерних узлов, после чего к ним применяется логическая операция, заданная значением текущего узла.

Необходимо вернуть логический результат вычисления корневого узла.

Полное бинарное дерево - это бинарное дерево, в котором каждый узел имеет либо 0, либо 2 потомка.
Листовой узел - это узел, не имеющий потомков.

Примеры:
Ввод: root = [2, 1, 3, null, null, 0, 1]
Вывод: True

Ввод: root = [0]
Вывод: False
'''

from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional['TreeNode']) -> bool:
        if root.left is None and root.right is None:
            return bool(root.val)

        left_result = self.evaluateTree(root.left)
        right_result = self.evaluateTree(root.right)

        if root.val == 2:
            return left_result or right_result
        else:
            return left_result and right_result