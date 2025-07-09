'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
    + MinStack() initializes the stack object;
    + void push(int value) pushes the element value onto the stack;
    + void pop() removes the element on the top of the stack;
    + int top() gets the top element of the stack;
    + int get_min() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Реализуйте стек MinStack:
    + MinStack() — инициализирует объект стека;
    + void push(int value) — помещает элемент value в стек;
    + void pop() — удаляет элемент с вершины стека;
    + int top() — возвращает верхний элемент стека;
    + int get_min() — возвращает минимальный элемент в стеке.

Все функции должны работать за O(1) времени.
'''

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> None:
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]