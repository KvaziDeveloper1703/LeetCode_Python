'''
Implement a Last-In-First-Out stack using only two queues. The stack should support all standard stack operations: push, pop, top, and empty.

Implement the MyStack class with the following methods:
    - void push(int x): push element x onto the top of the stack;
    - int pop(): removes the element on the top of the stack and returns it;
    - int top(): returns the element currently on the top of the stack;
    - boolean empty(): returns true if the stack is empty, otherwise returns false.

Example:
Input: ["MyStack", "push", "push", "top", "pop", "empty"], [[], [1], [2], [], [], []].
Output: [null, null, null, 2, 2, false].

Реализуйте стек (Last-In-First-Out, LIFO), используя только две очереди. Стек должен поддерживать все стандартные операции: push, pop, top и empty.

Реализуйте класс MyStack со следующими методами:
    - void push(int x): добавляет элемент x на вершину стека;
    - int pop(): удаляет элемент с вершины стека и возвращает его;
    - int top(): возвращает элемент, находящийся на вершине стека;
    - boolean empty(): возвращает true, если стек пуст, иначе false.

Пример:
Ввод: ["MyStack", "push", "push", "top", "pop", "empty"], [[], [1], [2], [], [], []].
Вывод: [null, null, null, 2, 2, false].
'''

from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top_element = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return top_element

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top_element = self.q1.popleft()
        self.q2.append(top_element)
        self.q1, self.q2 = self.q2, self.q1
        return top_element

    def empty(self) -> bool:
        return len(self.q1) == 0