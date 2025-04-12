'''
Design a data structure for a Least Recently Used (LRU) cache. Implement the LRUCache class with the following methods:
+ LRUCache(int capacity): Initializes the cache with a positive size capacity;
+ int get(int key): Returns the value of the key if it exists, otherwise returns -1;
+ void put(int key, int value): Updates the value of the key if it exists, or adds the key-value pair. If the cache exceeds capacity, evicts the least recently used key.

Both get and put must run in O(1) time complexity.

Разработайте структуру данных для кэша с вытеснением наименее недавно использованного элемента. Реализуйте класс LRUCache со следующими методами:
+ LRUCache(int capacity): Инициализирует кэш с положительной ёмкостью capacity;
+ int get(int key): Возвращает значение по ключу, если оно существует в кэше, иначе возвращает -1;
+ void put(int key, int value): Обновляет значение по ключу, если он уже существует, или добавляет новую пару ключ-значение.

Если при этом размер кэша превышает заданную ёмкость, то необходимо удалить наименее недавно использованный ключ.

Обе операции — get и put — должны выполняться за O(1) по времени.
'''

class ListNode:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_at_front(self, node: ListNode):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert_at_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._insert_at_front(node)
        else:
            if len(self.cache) == self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._insert_at_front(new_node)