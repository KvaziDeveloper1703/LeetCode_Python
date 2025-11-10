'''
You are given a stream of n pairs (idKey, value) arriving in arbitrary order, where:
    - idKey is an integer between 1 and n, and
    - value is a string.
No two pairs have the same idKey.

Design a data structure OrderedStream that returns values in increasing order of their IDs by producing a chunk (a list of consecutive values) after each insertion.

The concatenation of all the returned chunks should form the list of values sorted by their idKey.

Class Specification:
    - OrderedStream(int n): Initializes the stream to accept n values (IDs from 1 to n).
    - String[] insert(int idKey, String value): Inserts the pair (idKey, value) into the stream, and returns the largest possible chunk of values that can now be output in order, starting from the current smallest unreturned ID.

Examples:
Input: ["OrderedStream", "insert", "insert", "insert", "insert", "insert"], [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
Output: [null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]

Дан поток из n пар (idKey, value), которые поступают в произвольном порядке, где:
    - idKey - это целое число от 1 до n,
    - value - строка.
Гарантируется, что два элемента не имеют одинакового idKey.

Нужно спроектировать структуру данных OrderedStream, которая будет возвращать значения в возрастающем порядке ID, выдавая после каждого добавления фрагмент (chunk) — список подряд идущих элементов, которые теперь можно вернуть по порядку.

Объединение всех таких фрагментов в порядке вставки должно образовать полностью отсортированный список значений по их idKey.

Описание класса:
    - OrderedStream(int n): Создаёт поток, рассчитанный на n элементов (ID от 1 до n).
    - String[] insert(int idKey, String value): Вставляет пару (idKey, value) в поток и возвращает наибольший возможный фрагмент подряд идущих элементов, которые теперь можно вернуть начиная с текущего минимального невыданного ID.

Примеры:
Ввод: ["OrderedStream", "insert", "insert", "insert", "insert", "insert"], [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
Вывод: [null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]
'''

from typing import List

class OrderedStream:
    def __init__(self, n: int):
        self.stream = [None] * (n + 1)
        self.pointer = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        result = []

        while self.pointer < len(self.stream) and self.stream[self.pointer] is not None:
            result.append(self.stream[self.pointer])
            self.pointer += 1

        return result