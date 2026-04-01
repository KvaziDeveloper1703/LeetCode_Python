'''
You are given two binary trees: original and cloned, as well as a reference to a node target in the original tree.
The cloned tree is an exact copy of the original tree.
Return a reference to the corresponding node in the cloned tree that matches the given target node from the original tree.

Даны два бинарных дерева: original и cloned, а также ссылка на узел target в дереве original.
Дерево cloned является точной копией дерева original.
Необходимо вернуть ссылку на соответствующий узел в дереве cloned, который соответствует узлу target из дерева original.
'''

from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original is None:
            return None

        if original == target:
            return cloned

        left_result = self.getTargetCopy(original.left, cloned.left, target)
        if left_result is not None:
            return left_result

        return self.getTargetCopy(original.right, cloned.right, target)

def build_tree(values):
    if not values:
        return None

    nodes = []
    for value in values:
        if value is None:
            nodes.append(None)
        else:
            nodes.append(TreeNode(value))

    index = 0
    for i in range(len(values)):
        if nodes[i] is not None:
            left_index = 2 * i + 1
            right_index = 2 * i + 2

            if left_index < len(values):
                nodes[i].left = nodes[left_index]

            if right_index < len(values):
                nodes[i].right = nodes[right_index]

    return nodes[0]

def find_node(root, value):
    if root is None:
        return None

    if root.val == value:
        return root

    left_result = find_node(root.left, value)
    if left_result is not None:
        return left_result

    return find_node(root.right, value)

def copy_tree(root):
    if root is None:
        return None

    new_node = TreeNode(root.val)
    new_node.left = copy_tree(root.left)
    new_node.right = copy_tree(root.right)

    return new_node

values = [7, 4, 3, None, None, 6, 19]

original = build_tree(values)
cloned = copy_tree(original)

target = find_node(original, 3)

solution = Solution()
result = solution.getTargetCopy(original, cloned, target)

print(result.val)