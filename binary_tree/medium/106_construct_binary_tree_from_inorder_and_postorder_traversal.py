'''
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Constraints:
    + 1 <= inorder.length <= 3000;
    + postorder.length == inorder.length;
    + -3000 <= inorder[i], postorder[i] <= 3000;
    + inorder and postorder consist of unique values;
    + Each value of postorder also appears in inorder;
    + inorder is guaranteed to be the inorder traversal of the tree;
    + postorder is guaranteed to be the postorder traversal of the tree.

Даны два целочисленных массива — inorder и postorder, которые представляют симметричный (inorder) и обратный (postorder) обходы одного и того же бинарного дерева. Необходимо восстановить бинарное дерево по этим обходам и вернуть его корень.

Пример:
Ввод: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Вывод: [3,9,20,null,null,15,7]

Ограничения:
    + 1 <= длина inorder <= 3000;
    + inorder и postorder имеют одинаковую длину;
    + Значения элементов: от -3000 до 3000;
    + Все значения в массивах уникальны;
    + Все значения из postorder присутствуют в inorder;
    + inorder гарантированно представляет симметричный обход дерева;
    + postorder гарантированно представляет обратный обход того же дерева.
'''

from typing import List, Optional

class TreeNode:
    def __init__(self, value=0, left_child=None, right_child=None):
        self.value = value
        self.left = left_child
        self.right = right_child

def build_tree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    inorder_index_map = {value: index for index, value in enumerate(inorder)}
    postorder_index = len(postorder) - 1

    def build_subtree(inorder_left_index: int, inorder_right_index: int) -> Optional[TreeNode]:
        if inorder_left_index > inorder_right_index:
            return None

        root_value = postorder[postorder_index]
        postorder_index -= 1

        root = TreeNode(root_value)

        inorder_root_index = inorder_index_map[root_value]

        root.right = build_subtree(inorder_root_index + 1, inorder_right_index)
        root.left = build_subtree(inorder_left_index, inorder_root_index - 1)

        return root

    return build_subtree(0, len(inorder) - 1)