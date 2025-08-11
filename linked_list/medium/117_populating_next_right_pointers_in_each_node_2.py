'''
Given a binary tree where each node has the following structure:
struct Node {
  int value;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL. Initially, all next pointers are set to NULL.

Example:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]

Дано бинарное дерево, где каждый узел имеет следующую структуру:
struct Node {
  int value;
  Node *left;
  Node *right;
  Node *next;
}

Твоя задача — заполнить поле next для каждого узла, чтобы оно указывало на следующий узел справа на том же уровне. Если такого узла нет — установить next в NULL. Изначально все поля next установлены в NULL.

Пример:
Ввод: root = [1,2,3,4,5,null,7]
Вывод: [1,#,2,3,#,4,5,7,#]
'''

from collections import deque

class Node:
    def __init__(self, value: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.value = value
        self.left = left
        self.right = right
        self.next = next

def connect(root: 'Node') -> 'Node':
    if not root:
        return None

    node_queue = deque([root])

    while node_queue:
        level_size = len(node_queue)
        previous_node = None

        for _ in range(level_size):
            current_node = node_queue.popleft()

            if previous_node:
                previous_node.next = current_node
            previous_node = current_node

            if current_node.left:
                node_queue.append(current_node.left)
            if current_node.right:
                node_queue.append(current_node.right)

        previous_node.next = None

    return root