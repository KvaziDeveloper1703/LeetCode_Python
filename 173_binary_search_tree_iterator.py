'''
Implement the BSTIterator class that represents an iterator over the in-order traversal of a Binary Search Tree (BST).

Class methods:
+ BSTIterator(TreeNode root):
    + Initializes the BSTIterator object with the root of the BST;
    + The pointer is initialized to a non-existent value smaller than any element in the BST.

+ boolean has_next():
    + Returns true if there exists a next number in the in-order traversal to the right of the pointer; otherwise, returns false.

+ int next():
    + Moves the pointer to the right and returns the number at the pointer;
    + The first call to next() returns the smallest element in the BST.

Реализуй класс BSTIterator, который представляет итератор по бинарному дереву поиска (BST), итерирующийся в порядке симметричного обхода.

Методы класса:
+ BSTIterator(TreeNode root):
    + Инициализирует объект BSTIterator, принимая корень бинарного дерева поиска;
    + Указатель инициализируется на фиктивное значение, меньшее любого элемента в дереве.

+ boolean has_next():
    + Возвращает true, если существует следующий элемент справа от текущего указателя, иначе — false.

+ int next():
    + Перемещает указатель на следующий элемент в порядке in-order и возвращает его значение;
    + Первая вызванная функция next() вернёт наименьшее значение в дереве.
'''

from typing import Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BSTIterator:
    
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left_branch(root)

    def _push_left_branch(self, node: Optional[TreeNode]):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        current_node = self.stack.pop()
        result = current_node.value

        if current_node.right:
            self._push_left_branch(current_node.right)

        return result

    def has_next(self) -> bool:
        return len(self.stack) > 0