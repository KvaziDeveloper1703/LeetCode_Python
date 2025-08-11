'''
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
Answers within 10⁻⁵ of the actual answer will be accepted.

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000, 14.50000, 11.00000]

Дано бинарное дерево. Необходимо вернуть среднее значение всех узлов на каждом уровне дерева в виде массива чисел с плавающей точкой.
Ответы с точностью до 10⁻⁵ от правильного значения считаются допустимыми.

Пример:
Ввод: root = [3,9,20,null,null,15,7]
Вывод: [3.00000, 14.50000, 11.00000]
'''

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def average_of_levels(root: Optional[TreeNode]) -> List[float]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_sum = 0

        for _ in range(level_size):
            current_node = queue.popleft()
            level_sum += current_node.value

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        average = level_sum / level_size
        result.append(average)

    return result