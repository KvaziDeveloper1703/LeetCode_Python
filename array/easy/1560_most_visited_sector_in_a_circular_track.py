'''
Given an integer n and an integer array rounds.

There is a circular track with n sectors, labeled from 1 to n. A marathon will be held on this track, consisting of several rounds.
    + The i-th round starts at sector rounds[i - 1] and ends at sector rounds[i];
    + For example, round 1 starts at rounds[0] and ends at rounds[1];
    + Movement is always in ascending order of sector numbers.

Return an array of the most visited sectors, sorted in ascending order.

Examples:
Input: n = 4, rounds = [1,3,1,2]
Output: [1,2]

Input: n = 2, rounds = [2,1,2,1,2,1,2,1,2]
Output: [2]

Дано целое число n и массив целых чисел rounds.

Есть круговая трасса, состоящая из n секторов, пронумерованных от 1 до n. На этой трассе проводится марафон, который состоит из нескольких этапов.
    + i-й раунд начинается в секторе rounds[i - 1] и заканчивается в секторе rounds[i];
    + Например, первый раунд начинается в rounds[0] и заканчивается в rounds[1];
    + Движение всегда идёт в порядке возрастания номеров секторов.

Нужно вернуть массив самых посещаемых секторов, отсортированный по возрастанию.

Примеры:
Ввод: n = 4, rounds = [1,3,1,2]
Вывод: [1,2]

Ввод: n = 2, rounds = [2,1,2,1,2,1,2,1,2]
Вывод: [2]
'''

from typing import List

def most_visited(n: int, rounds: List[int]) -> List[int]:
    first_sector = rounds[0]
    last_sector = rounds[-1]

    most_visited_sectors = []

    if first_sector <= last_sector:
        for sector in range(first_sector, last_sector + 1):
            most_visited_sectors.append(sector)
    else:
        for sector in range(1, last_sector + 1):
            most_visited_sectors.append(sector)
        for sector in range(first_sector, n + 1):
            most_visited_sectors.append(sector)

    return most_visited_sectors