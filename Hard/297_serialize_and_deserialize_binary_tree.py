'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection, to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You simply need to ensure that a binary tree can be serialized into a string and this string can then be deserialized back into the original tree structure.

Clarification:
The input/output format is the same as how LeetCode serializes a binary tree.
However, you do not necessarily need to follow this format exactly, so you are encouraged to be creative and come up with your own approach.

Examples:
Input:  root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Сериализация — это процесс преобразования структуры данных или объекта в последовательность битов, чтобы их можно было сохранить в файле или буфере памяти, либо передать по сети для последующего восстановления в той же или другой среде.
Необходимо разработать алгоритм для сериализации и десериализации бинарного дерева. Ограничений на то, как именно должна работать ваша схема сериализации/десериализации, нет.
Вам нужно лишь гарантировать, что бинарное дерево может быть преобразовано в строку (сериализовано), а затем эта строка может быть обратно преобразована в исходную структуру дерева (десериализовано).

Уточнение:
Входной и выходной форматы такие же, как у LeetCode для сериализации бинарных деревьев.
Однако вам не обязательно точно следовать этому формату — можете проявить креативность и предложить свой собственный подход.

Примеры:
Ввод:  root = [1,2,3,null,null,4,5]
Вывод: [1,2,3,null,null,4,5]
'''

class TreeNode(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        def helper(node):
            if node is None:
                values.append('None')
            else:
                values.append(str(node.value))
                helper(node.left)
                helper(node.right)

        values = []
        helper(root)

        return ','.join(vals)

    def deserialize(self, data):
        def helper():
            value = next(values)
            if value == 'None':
                return None

            node = TreeNode(int(value))
            node.left = helper()
            node.right = helper()

            return node

        values = iter(data.split(','))
        return helper()