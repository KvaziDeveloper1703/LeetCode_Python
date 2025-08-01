'''
Given an array of integers stones, where stones[i] represents the weight of the i‑th stone.

We play a game with these stones:
    + On each turn, choose the two heaviest stones and smash them together.
    + Let the weights of these two stones be x and y, where x <= y.
        + If x == y, both stones are destroyed.
        + If x != y, the stone of weight x is destroyed, and the stone of weight y now has weight y - x.

The game continues until there is at most one stone left.
Return the weight of the last remaining stone. If no stones are left, return 0.

Examples:
Input: stones = [2,7,4,1,8,1]
Output: 1

Input: stones = [1]
Output: 1

Дан массив целых чисел stones, где stones[i] — вес i‑го камня.

Игра проходит так:
    + На каждом ходу выбираются два самых тяжёлых камня и сталкиваются друг с другом.
    + Пусть их веса — x и y, где x <= y.
        + Если x == y, оба камня уничтожаются.
        + Если x != y, камень весом x уничтожается, а камень весом y получает новый вес y - x.

Игра продолжается, пока не останется не более одного камня.
Верните вес последнего оставшегося камня. Если камней не осталось, верните 0.

Примеры:
Ввод: stones = [2,7,4,1,8,1]
Вывод: 1

Ввод: stones = [1]
Вывод: 1
'''

from typing import List
import heapq

def last_stone_weight(stones: List[int]) -> int:
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        y = -heapq.heappop(stones)
        x = -heapq.heappop(stones)

        if y != x:
            heapq.heappush(stones, -(y - x))

    return -stones[0] if stones else 0