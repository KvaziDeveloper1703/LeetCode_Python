'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes p and q.

According to Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in the tree T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Examples:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2

Дано дерево поиска (BST). Найдите наименьшего общего предка (LCA) для двух заданных узлов p и q.

Согласно определению с Википедии:
“Наименьший общий предок — это самый низкий узел в дереве T, который имеет оба узла p и q в качестве потомков (разрешается считать, что узел является потомком самого себя).”

Примеры:
Ввод: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Вывод: 6

Ввод: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Вывод: 2
'''

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root

        while current:
            if p.value < current.value and q.value < current.value:
                current = current.left
            elif p.value > current.value and q.value > current.value:
                current = current.right
            else:
                return current