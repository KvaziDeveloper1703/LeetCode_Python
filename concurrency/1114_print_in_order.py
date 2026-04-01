'''
Suppose we have a class:
public class Foo {
    public void first() { print("first"); }
    public void second() { print("second"); }
    public void third() { print("third"); }
}

The same instance of Foo will be passed to three different threads:
    - Thread A will call first();
    - Thread B will call second();
    - Thread C will call third().

Design a mechanism and modify the program to ensure that:
    - second() is executed after first();
    - third() is executed after second().

Examples:
Input: nums = [1,2,3]
Output: "firstsecondthird"

Examples:
Input: nums = [1,3,2]
Output: "firstsecondthird"

Дан класс:
public class Foo {
    public void first() { print("first"); }
    public void second() { print("second"); }
    public void third() { print("third"); }
}

Один и тот же экземпляр класса Foo передаётся в три разных потока:
    - Поток A вызывает first();
    - Поток B вызывает second();
    - Поток C вызывает third().

Необходимо реализовать механизм и изменить программу так, чтобы:
    - метод second() выполнялся после first();
    - метод third() выполнялся после second().

Примеры:
Ввод: nums = [1,2,3]
Вывод: "firstsecondthird"

Ввод: nums = [1,3,2]
Вывод: "firstsecondthird"
'''

from threading import Lock, Thread

class Foo:
    def __init__(self):
        self.lock_second = Lock()
        self.lock_third = Lock()
        self.lock_second.acquire()
        self.lock_third.acquire()

    def first(self, printFirst):
        printFirst()
        self.lock_second.release()

    def second(self, printSecond):
        self.lock_second.acquire()
        printSecond()
        self.lock_third.release()

    def third(self, printThird):
        self.lock_third.acquire()
        printThird()

def printFirst():
    print("first", end="")

def printSecond():
    print("second", end="")

def printThird():
    print("third", end="")

foo = Foo()

thread1 = Thread(target=foo.first, args=(printFirst,))
thread2 = Thread(target=foo.second, args=(printSecond,))
thread3 = Thread(target=foo.third, args=(printThird,))

thread3.start()
thread2.start()
thread1.start()

thread1.join()
thread2.join()
thread3.join()