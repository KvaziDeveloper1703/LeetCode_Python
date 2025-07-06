'''
Design an iterator that supports the peek operation in addition to the standard next() and hasNext() operations.
Implement the PeekingIterator class:
    + PeekingIterator(Iterator<int> nums) — Initializes the object with the given integer iterator.
    + int next() — Returns the next element in the array and moves the pointer forward.
    + boolean hasNext() — Returns true if there are more elements.
    + int peek() — Returns the next element without advancing the iterator.

Note: Each language may implement Iterator differently, but all of them must support int next() and boolean hasNext().

Example:
Input: ["PeekingIterator", "next", "peek", "next", "next", "hasNext"], [[[1, 2, 3]], [], [], [], [], []]
Output: [null, 1, 2, 2, 3, false]

Спроектируйте итератор, который поддерживает операцию подглядывания (peek) в дополнение к обычным методам next() и hasNext().
Реализуйте класс PeekingIterator с методами:
    + PeekingIterator(Iterator<int> nums) — инициализирует объект переданным итератором целых чисел.
    + int next() — возвращает следующий элемент и продвигает указатель.
    + boolean hasNext() — возвращает true, если остались элементы.
    + int peek() — возвращает следующий элемент, не продвигая указатель.

Примечание: В разных языках итераторы реализуются по-разному, но обязательно должны поддерживать методы int next() и boolean hasNext().

Пример:
Ввод: ["PeekingIterator", "next", "peek", "next", "next", "hasNext"], [[[1, 2, 3]], [], [], [], [], []]
Вывод: [null, 1, 2, 2, 3, false]
'''

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self._next_element = self.iterator.next() if self.iterator.hasNext() else None
        self._has_next = self._next_element is not None

    def peek(self):
        return self._next_element

    def next(self):
        current = self._next_element
        if self.iterator.hasNext():
            self._next_element = self.iterator.next()
        else:
            self._next_element = None
        self._has_next = self._next_element is not None
        return current

    def hasNext(self):
        return self._has_next