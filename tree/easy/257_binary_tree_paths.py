'''
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node that has no children.

Examples:
Input: root = [1,2,3,null,5]
Output: ["1->2->5", "1->3"]

Input: root = [1]
Output: ["1"]

Дан корень бинарного дерева. Верните все пути от корня до листа в любом порядке.

Лист - это узел, у которого нет дочерних узлов.

Примеры:
Ввод: root = [1,2,3,null,5]
Вывод: ["1->2->5", "1->3"]

Ввод: root = [1]
Вывод: ["1"]
'''

from typing import Optional, List

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []

        result_paths: List[str] = []

        def depth_first_search(current_node: TreeNode, current_path: str) -> None:
            if current_node.left is None and current_node.right is None:
                result_paths.append(current_path)
                return

            if current_node.left is not None:
                depth_first_search(
                    current_node.left,
                    current_path + "->" + str(current_node.left.val)
                )

            if current_node.right is not None:
                depth_first_search(
                    current_node.right,
                    current_path + "->" + str(current_node.right.val)
                )

        depth_first_search(root, str(root.val))
        return result_paths