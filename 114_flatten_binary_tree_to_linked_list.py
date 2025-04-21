'''
Given the root of a binary tree, flatten the tree into a "linked list":
+ The "linked list" should use the same TreeNode class, where:
    + The right child pointer points to the next node in the list,
    + The left child pointer is always null.

The linked list should be in the same order as a pre-order traversal of the binary tree.

Example:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Дано бинарное дерево. Требуется преобразовать его в "связанный список", где:
+ Каждая вершина дерева должна быть преобразована так, чтобы:
    + Указатель right указывает на следующий элемент списка,
    + Указатель left всегда равен null.

При этом порядок элементов в списке должен соответствовать прямому обходу (preorder traversal) исходного дерева.

Пример: 
Ввод: root = [1,2,5,3,4,null,6]
Вывод: [1,null,2,null,3,null,4,null,5,null,6]
'''

from typing import Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        node_stack = [root]

        while node_stack:
            current_node = node_stack.pop()

            if current_node.right:
                node_stack.append(current_node.right)
            if current_node.left:
                node_stack.append(current_node.left)

            if node_stack:
                current_node.right = node_stack[-1]
            current_node.left = None