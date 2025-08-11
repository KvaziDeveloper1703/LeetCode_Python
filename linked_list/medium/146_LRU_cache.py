'''
Design a data structure for a Least Recently Used cache. Implement the LRUCache class with the following methods:
    + LRUCache(int capacity): Initializes the cache with a positive size capacity;
    + int get(int key): Returns the value of the key if it exists, otherwise returns -1;
    + void put(int key, int value): Updates the value of the key if it exists, or adds the key-value pair. If the cache exceeds capacity, evicts the least recently used key.

Both get and put must run in O(1) time complexity.

Разработайте структуру данных для кэша с вытеснением наименее недавно использованного элемента. Реализуйте класс LRUCache со следующими методами:
    + LRUCache(int capacity): Инициализирует кэш с положительной ёмкостью capacity;
    + int get(int key): Возвращает значение по ключу, если оно существует в кэше, иначе возвращает -1;
    + void put(int key, int value): Обновляет значение по ключу, если он уже существует, или добавляет новую пару ключ-значение. Если при этом размер кэша превышает заданную ёмкость, то необходимо удалить наименее недавно использованный ключ.

Обе операции — get и put — должны выполняться за O(1) по времени.
'''

from collections import OrderedDict

class ListNode:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)