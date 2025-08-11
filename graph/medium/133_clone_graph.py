'''
You are given a reference to a node in a connected undirected graph:
class Node:
    value: int
    neighbors: List[Node]

Return a deep copy of the graph starting from that node (value = 1).
The graph may have cycles and is represented as an adjacency list.

Дан указатель на узел связного неориентированного графа. Каждый узел содержит:
class Node:
    value: int
    neighbors: List[Node]

Нужно создать и вернуть глубокую копию графа, начиная с этого узла (value = 1).
Граф представлен списком смежности, узлы могут образовывать циклы.
'''

from typing import List, Dict

class Node:
    def __init__(self, value: int = 0, neighbors: List['Node'] = None):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node: 'Node') -> 'Node':
    if not node:
        return None

    cloned_nodes: Dict[int, Node] = {}

    def dfs(current_node: 'Node') -> 'Node':
        if current_node.value in cloned_nodes:
            return cloned_nodes[current_node.value]

        copy = Node(current_node.value)
        cloned_nodes[current_node.value] = copy

        for neighbor in current_node.neighbors:
            copy.neighbors.append(dfs(neighbor))

        return copy

    return dfs(node)