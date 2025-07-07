'''
Implement a first-in-first-out queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
Implement the MyQueue class with the following methods:
    + void push(): Pushes element x to the back of the queue;
    + int pop(): Removes the element from the front of the queue and returns it;
    + int peek(): Returns the element at the front of the queue;
    + boolean empty(): Returns true if the queue is empty, otherwise returns false.

Notes:
    + You must use only standard operations of a stack, meaning: push to top, pop from top, peek from top, check size, and check if empty.
    + If your language does not support stacks natively, you may simulate a stack using a list or a deque — as long as you only use standard stack operations.

Example:
Input: ["MyQueue", "push", "push", "peek", "pop", "empty"], [[], [1], [2], [], [], []]
Output: [null, null, null, 1, 1, false]

Реализуйте очередь, используя только два стека. Реализованная очередь должна поддерживать все стандартные операции: push, peek, pop, и empty.
Реализуйте класс MyQueue с методами:
    + void push(int x): Добавляет элемент x в конец очереди;
    + int pop(): Удаляет элемент из начала очереди и возвращает его;
    + int peek(): Возвращает элемент из начала очереди, не удаляя его;
    + boolean empty(): Возвращает true, если очередь пуста, иначе false.

Примечания:
    + Разрешено использовать только стандартные операции со стеком: добавление на вершину (push), удаление с вершины (pop), просмотр вершины (peek), проверка размера и пустоты.
    + Если в вашем языке нет встроенного типа данных "стек", можно использовать список или двустороннюю очередь (deque) — но только с операциями, допустимыми для стека.

Пример:
Ввод: ["MyQueue", "push", "push", "peek", "pop", "empty"], [[], [1], [2], [], [], []]
Вывод: [null, null, null, 1, 1, false]
'''

class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self.move()
        return self.stack_out.pop()

    def peek(self) -> int:
        self.move()
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out

    def move(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())