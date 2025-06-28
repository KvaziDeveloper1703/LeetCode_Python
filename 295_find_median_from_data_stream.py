'''
The median is the middle value in an ordered list of integers.
If the list has an even number of elements, there is no single middle value, so the median is defined as the mean of the two middle values.

For example:
    + For arr = [2,3,4], the median is 3.
    + For arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class with the following methods:
    + MedianFinder() initializes the MedianFinder object.
    + void addNum(int num) adds the integer num from the data stream to the data structure.
    + double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer are considered correct.

Example:
Input:
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]

Output:
[null, null, null, 1.5, null, 2.0]

Медиана — это среднее значение в упорядоченном списке целых чисел.
Если размер списка чётный, то медианы как одного среднего значения нет, и медианой считается среднее арифметическое двух средних элементов.

Например:
    + Для arr = [2,3,4] медиана равна 3.
    + Для arr = [2,3] медиана равна (2 + 3) / 2 = 2.5.

Необходимо реализовать класс MedianFinder со следующими методами:
    + MedianFinder() — инициализирует объект MedianFinder.
    + void addNum(int num) — добавляет целое число num из потока данных в структуру данных.
    + double findMedian() — возвращает медиану всех добавленных на данный момент элементов. Ответы с точностью до 10^-5 от правильного считаются верными.

Пример:
Ввод:
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]

Вывод:
[null, null, null, 1.5, null, 2.0]
'''

import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2.0