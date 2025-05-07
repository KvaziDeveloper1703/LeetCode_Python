'''
Given the head of a singly linked list where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
A height-balanced BST is defined as a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]

Дан head односвязного списка, элементы которого отсортированы по возрастанию. Преобразуйте его в сбалансированное бинарное дерево поиска.
Сбалансированное по высоте дерево — это бинарное дерево, в котором глубина двух поддеревьев любого узла отличается не более чем на один.

Примеры:
Ввод: head = [-10,-3,0,5,9]
Вывод: [0,-3,9,-10,null,5]
'''

from typing import Optional

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.value)

        def find_middle(head):
            previous = None
            slow = fast = head
            while fast and fast.next:
                previous = slow
                slow = slow.next
                fast = fast.next.next
            if previous:
                previous.next = None
            return slow

        mid = find_middle(head)
        root = TreeNode(mid.value)

        if head != mid:
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root