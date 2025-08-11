'''
Design a HashMap without using any built-in hash table libraries.

Implement a class called MyHashMap with the following methods:
    + MyHashMap() – Initializes the object with an empty map;
    + void put(int key, int value) – Inserts a (key, value) pair into the HashMap. If the key already exists, update the corresponding value;
    + int get(int key) – Returns the value associated with the specified key, or -1 if the key is not in the map;
    + void remove(int key) – Removes the key and its corresponding value if it exists in the map.

Example:
Input: ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"], [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output: [null, null, null, 1, -1, null, 1, null, -1]

Реализуйте структуру данных HashMap без использования встроенных хэш-таблиц.

Создайте класс MyHashMap с методами:
    + MyHashMap() – Инициализирует объект пустой хэш-картой;
    + void put(int key, int value) – Вставляет пару (ключ, значение) в карту. Если ключ уже существует, обновляет соответствующее значение;
    + int get(int key) – Возвращает значение, связанное с данным ключом, или -1, если такой ключ отсутствует;
    + void remove(int key) – Удаляет ключ и связанное с ним значение, если такая пара существует.

Пример:
Ввод: ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"], [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Вывод: [null, null, null, 1, -1, null, 1, null, -1]
'''

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                return
        self.buckets[index].append((key, value))

    def get(self, key: int) -> int:
        index = self._hash(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        self.buckets[index] = [(k, v) for k, v in self.buckets[index] if k != key]