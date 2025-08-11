'''
Design a HashSet without using any built-in hash table libraries.

Implement a class called MyHashSet with the following methods:
    + void add(key) – Inserts the value key into the HashSet;
    + bool contains(key) – Returns true if the key exists in the HashSet, otherwise false;
    + void remove(key) – Removes the value key from the HashSet. If the key does not exist, do nothing.

Example:
Input: ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"], [[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output: [null, null, null, true, false, null, true, null, false]

Реализуйте структуру данных HashSet без использования встроенных хэш-таблиц.

Создайте класс MyHashSet с методами:
    + void add(key) – Добавляет элемент key во множество;
    + bool contains(key) – Возвращает true, если key содержится во множестве, иначе false;
    + void remove(key) – Удаляет элемент key из множества. Если элемент не найден — ничего не делать.

Пример:
Ввод: ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"], [[], [1], [2], [1], [3], [2], [2], [2], [2]]
Вывод: [null, null, null, true, false, null, true, null, false]
'''

class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        index = self._hash(key)
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        return key in self.buckets[index]