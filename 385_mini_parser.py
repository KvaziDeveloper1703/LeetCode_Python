'''
You are given a string S that represents the serialization of a nested list. Implement a parser to deserialize it and return the corresponding NestedInteger object.

Each element is either:
    + a single integer, or
    + a list, whose elements can themselves be integers or other nested lists.

Example:
Input: S = "324"
Output: 324

Вам дана строка S, представляющая сериализованный вложенный список. Реализуйте парсер, который десериализует эту строку и возвращает объект NestedInteger.

Каждый элемент может быть:
    + либо целым числом,
    + либо списком, элементы которого также могут быть числами или другими вложенными списками.

Пример:
Ввод: S = "324"
Вывод: 324
'''

from typing import Union, List

class NestedInteger:
    def __init__(self, value: Union[int, None] = None):
        if value is None:
            self._integer = None
            self._list = []
        else:
            self._integer = value
            self._list = None

    def isInteger(self) -> bool:
        return self._integer is not None

    def setInteger(self, value: int):
        self._integer = value
        self._list = None

    def add(self, elem: 'NestedInteger'):
        if self._list is None:
            self._list = []
        self._list.append(elem)

    def getInteger(self) -> Union[int, None]:
        return self._integer

    def getList(self) -> Union[List['NestedInteger'], None]:
        return self._list

    def __repr__(self):
        if self.isInteger():
            return str(self._integer)
        return '[' + ', '.join(repr(e) for e in self._list) + ']'

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s:
            return NestedInteger()

        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        number_buffer = ''

        for character in s:
            if character == '[':
                stack.append(NestedInteger())
            elif character == '-' or character.isdigit():
                number_buffer += character
            elif character == ',' or character == ']':
                if number_buffer:
                    number = int(number_buffer)
                    stack[-1].add(NestedInteger(number))
                    number_buffer = ''
                if character == ']' and len(stack) > 1:
                    finished = stack.pop()
                    stack[-1].add(finished)

        return stack[0]