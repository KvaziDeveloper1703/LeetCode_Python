'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Constraints:
    + 1 <= preorder.length <= 3000;
    + inorder.length == preorder.length;
    + -3000 <= preorder[i], inorder[i] <= 3000;
    + preorder and inorder consist of unique values;
    + Each value of inorder also appears in preorder;
    + preorder is guaranteed to be the preorder traversal of the tree;
    + inorder is guaranteed to be the inorder traversal of the tree.

Даны два целочисленных массива — preorder и inorder, которые представляют прямой (preorder) и симметричный (inorder) обходы одного и того же бинарного дерева. Необходимо восстановить бинарное дерево по этим обходам и вернуть его корень.

Пример:
Ввод: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Вывод: [3,9,20,null,null,15,7]

Ограничения:
    + 1 <= длина preorder <= 3000;
    + inorder и preorder имеют одинаковую длину;
    + Значения элементов: от -3000 до 3000;
    + Все значения в массивах уникальны;
    + Все значения из inorder присутствуют в preorder;
    + preorder гарантированно представляет прямой обход дерева;
    + inorder гарантированно представляет симметричный обход того же дерева.
'''

from typing import List, Optional

class TreeNode:
    def __init__(self, value=0, left_child=None, right_child=None):
        self.value = value
        self.left = left_child
        self.right = right_child

def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    inorder_index_map = {value: index for index, value in enumerate(inorder)}

    def build_subtree(preorder_left_index: int, preorder_right_index: int,
        inorder_left_index: int, inorder_right_index: int) -> Optional[TreeNode]:
        if preorder_left_index > preorder_right_index:
            return None

        root_value = preorder[preorder_left_index]
        root = TreeNode(root_value)

        inorder_root_index = inorder_index_map[root_value]

        left_subtree_size = inorder_root_index - inorder_left_index

        root.left = build_subtree(  preorder_left_index + 1,
                                    preorder_left_index + left_subtree_size,
                                    inorder_left_index,
                                    inorder_root_index - 1)

        root.right = build_subtree( preorder_left_index + left_subtree_size + 1,
                                    preorder_right_index,
                                    inorder_root_index + 1,
                                    inorder_right_index)

        return root

    return build_subtree(0, len(preorder) - 1, 0, len(inorder) - 1)