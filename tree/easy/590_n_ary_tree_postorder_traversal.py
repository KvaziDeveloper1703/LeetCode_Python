'''
You are given the root of an n-ary tree.
Your task is to return the postorder traversal of the node values.

Definition:
    - In an n-ary tree, each node can have zero or more children.
    - Postorder traversal means:
        - First recursively visit all children of the node from left to right;
        - Then visit the current node.

Input format:
The tree is represented using level-order traversal:
    - Nodes are listed level by level;
    - Groups of children are separated by null.

Return a list of node values in postorder traversal order.

Дан корень n-арного дерева.
Необходимо вернуть обратный обход значений узлов.

Определение:
    - В n-арном дереве каждый узел может иметь любое количество потомков;
    - Обратный обход выполняется так:
        - Сначала рекурсивно обходятся все потомки узла слева направо;
        - Затем посещается сам узел.

Формат входных данных:
Дерево задано в виде обхода по уровням:
    - Узлы перечислены по уровням;
    - Группы детей разделяются значением null.

Вернуть список значений узлов в порядке postorder обхода.
'''

from typing import List, Optional

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []

        def dfs(node):
            if not node:
                return

            for child in node.children or []:
                dfs(child)

            result.append(node.val)

        dfs(root)
        return result