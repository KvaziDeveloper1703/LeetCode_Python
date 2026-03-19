'''
You are given the root of an n-ary tree.
Your task is to return the preorder traversal of the node values.

Definition:
    - In an n-ary tree, each node can have zero or more children;
    - Preorder traversal means:
        - Visit the current node;
        - Then recursively visit all its children from left to right.

Input format:
The tree is represented using level-order traversal:
    - Values are listed level by level;
    - Groups of children are separated by null.

Return a list of node values in preorder traversal order.

Дан корень n-арного дерева.
Необходимо вернуть прямой обход значений узлов.

Определение:
    - В n-арном дереве каждый узел может иметь произвольное количество потомков;
    - Прямой обход (preorder) выполняется так:
        - Сначала посещается текущий узел;
        - Затем рекурсивно обходятся все его потомки слева направо.

Формат входных данных:
Дерево задано в виде обхода по уровням:
    - Узлы перечислены по уровням;
    - Группы детей разделяются значением null.

Вернуть список значений узлов в порядке preorder обхода.
'''

from typing import List, Optional

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            for child in reversed(node.children):
                stack.append(child)

        return result