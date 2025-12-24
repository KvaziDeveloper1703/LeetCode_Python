'''
You are given an integer array gifts, where each element represents the number of gifts in a pile. You are also given an integer k.

Every second, you perform the following operation:
    - Choose the pile that currently has the maximum number of gifts. If there are multiple piles with the same maximum number of gifts, you may choose any of them;
    - Replace the number of gifts in the chosen pile with the floor value of the square root of its original number of gifts.

After performing this operation for k seconds, return the total number of gifts remaining in all piles.

Examples:
Input: gifts = [25, 64, 9, 4, 100], k = 4
Output: 29

Input: gifts = [1, 1, 1, 1], k = 4
Output: 4

Дан массив целых чисел gifts, где каждый элемент обозначает количество подарков в одной куче. Также дано целое число k.

Каждую секунду выполняется следующая операция:
    - Выбирается куча с наибольшим количеством подарков. Если таких куч несколько, можно выбрать любую из них;
    - Количество подарков в выбранной куче заменяется на целую часть квадратного корня от исходного количества подарков.

После выполнения этой операции k раз необходимо вернуть общее количество подарков, оставшихся во всех кучах.

Примеры:
Ввод: gifts = [25, 64, 9, 4, 100], k = 4
Вывод: 29

Ввод: gifts = [1, 1, 1, 1], k = 4
Вывод: 4
'''

from typing import List
import heapq
import math

def pick_gifts(gifts: List[int], k: int) -> int:
    maximum_heap = [-gift for gift in gifts]
    heapq.heapify(maximum_heap)

    for _ in range(k):
        largest_gift_pile = -heapq.heappop(maximum_heap)
        reduced_gift_pile = int(math.sqrt(largest_gift_pile))
        heapq.heappush(maximum_heap, -reduced_gift_pile)

    return -sum(maximum_heap)