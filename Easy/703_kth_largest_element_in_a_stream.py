'''
You are working in a university admissions office and need to keep track of the kth highest test score among applicants in real-time. This is to dynamically determine the cut-off mark for interviews and admissions as new applicants submit their scores.

Implement a class KthLargest that:
    + KthLargest(int k, int[] numbers): Initializes the object with the integer k and the initial stream of test scores numbers;
    + int add(int value): Adds a new test score value to the stream and returns the kth largest score among all scores seen so far.

Examples:
Input: ["KthLargest", "add", "add", "add", "add", "add"], [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output: [null, 4, 5, 5, 8, 8]

Input: ["KthLargest", "add", "add", "add", "add"], [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]
Output: [null, 7, 7, 7, 8]

Вы работаете в приёмной комиссии университета и должны в реальном времени отслеживать k-й по величине балл среди всех заявителей. Это нужно для того, чтобы динамически определять проходной балл для приглашения на собеседования и поступления, когда поступают новые результаты.

Необходимо реализовать класс KthLargest, который поддерживает такой функционал:
    + KthLargest(int k, int[] numbers): Инициализирует объект значением k и начальным списком баллов numbers;
    + int add(int value): Добавляет новый результат value в поток данных и возвращает k-й по величине балл среди всех результатов, полученных до этого момента.

Примеры:
Ввод: ["KthLargest", "add", "add", "add", "add", "add"], [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Вывод: [null, 4, 5, 5, 8, 8]

Ввод: ["KthLargest", "add", "add", "add", "add"], [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]
Вывод: [null, 7, 7, 7, 8]
'''

import heapq

class KthLargest:
    def __init__(self, k: int, numbers: list[int]):
        self.k = k
        self.heap = numbers
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, value: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, value)
        else:
            if value > self.heap[0]:
                heapq.heapreplace(self.heap, value)
        return self.heap[0]