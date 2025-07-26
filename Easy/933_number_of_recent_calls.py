'''
You are to implement a class called RecentCounter that counts the number of recent requests within a rolling time window of 3000 milliseconds.

Implement the following:
    + RecentCounter() - Initializes the counter. Initially, there are no requests.
    + int ping(int t) - Adds a new request at time t (measured in milliseconds). Returns the number of requests that have occurred in the last 3000 milliseconds, including the current one. That is, return the number of requests with timestamp in the inclusive range [t - 3000, t].

Example:
Input: ["RecentCounter", "ping", "ping", "ping", "ping"], [[], [1], [100], [3001], [3002]]
Output: [null, 1, 2, 3, 3]

Вам нужно реализовать класс RecentCounter, который считает количество недавних запросов в скользящем окне 3000 миллисекунд.

Реализуйте следующее:
    + RecentCounter() - Инициализирует счётчик. Изначально нет ни одного запроса.
    + int ping(int t) - Добавляет новый запрос во времени t (в миллисекундах). Возвращает количество запросов, которые произошли за последние 3000 миллисекунд, включая текущий. То есть нужно вернуть количество запросов с временными метками в диапазоне [t - 3000, t], включая границы.

Пример:
Ввод: ["RecentCounter", "ping", "ping", "ping", "ping"], [[], [1], [100], [3001], [3002]]
Вывод: [null, 1, 2, 3, 3]
'''

from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)