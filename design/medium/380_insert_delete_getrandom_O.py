'''
Design and implement a class RandomizedSet that supports inserting, removing, and retrieving random elements—all in average O(1) time complexity.
    + The class should be initialized using RandomizedSet();
    + The insert(value) method inserts an element value into the set if it is not already present. It returns true if the element was successfully inserted and false if it already exists;
    + The remove(value) method removes the element value from the set if it is present. It returns true if the element was removed and false if it was not found;
    + The getRandom() method returns a random element from the current set. It is guaranteed that at least one element exists when this method is called, and each element must have an equal probability of being returned.

All operations must run in average O(1) time.

Разработайте и реализуйте класс RandomizedSet, который поддерживает операции вставки, удаления и получения случайного элемента — в среднем за O(1) времени.
Класс должен поддерживать следующие методы:
    + RandomizedSet() — инициализирует объект множества;
    + insert(value) — вставляет элемент value в множество, если он ещё не присутствует. Возвращает true, если элемент был успешно вставлен, и false, если он уже существует;
    + remove(value) — удаляет элемент value из множества, если он присутствует. Возвращает true, если элемент был удалён, и false, если его не было в множестве;
    + getRandom() — возвращает случайный элемент из текущего множества. Гарантируется, что при вызове этого метода в множестве присутствует хотя бы один элемент, и каждый элемент должен иметь равную вероятность быть выбранным.

Все операции должны выполняться в среднем за O(1) времени.
'''

import random

class RandomizedSet:
    def __init__(self):
        self.value_to_index_map = {}
        self.value_list = []

    def insert(self, value: int) -> bool:
        if value in self.value_to_index_map:
            return False

        self.value_list.append(value)
        self.value_to_index_map[value] = len(self.value_list) - 1

        return True

    def remove(self, value: int) -> bool:
        if value not in self.value_to_index_map:
            return False

        index_to_remove = self.value_to_index_map[value]
        last_value = self.value_list[-1]

        self.value_list[index_to_remove] = last_value
        self.value_to_index_map[last_value] = index_to_remove
        self.value_list.pop()
    
        del self.value_to_index_map[value]

        return True

    def get_random(self) -> int:
        return random.choice(self.value_list)