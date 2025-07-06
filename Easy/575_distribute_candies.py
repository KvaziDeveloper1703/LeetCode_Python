'''
Alice has n candies, where the i-th candy is of type candyType[i].
Alice noticed that she was starting to gain weight, so she visited a doctor. The doctor advised her to eat only n / 2 of the candies she has (it is guaranteed that n is always even).
Alice loves her candies very much and wants to eat the maximum number of different types of candies possible while still following the doctor's advice.

Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 candies.

Examples:
Input: candyType = [1,1,2,2,3,3]
Output: 3

Input: candyType = [1,1,2,3]
Output: 2

У Алисы есть n конфет, при этом i-я конфета относится к типу candyType[i].
Алиса заметила, что начала набирать вес, и поэтому пошла к врачу. Врач посоветовал Алисе съесть только n / 2 конфет (гарантируется, что n всегда чётное).
Алиса очень любит свои конфеты и хочет съесть максимально возможное количество различных типов конфет, при этом следуя совету врача.

По данному целочисленному массиву candyType длины n, необходимо вернуть максимальное количество различных типов конфет, которые Алиса может съесть, если съест только n / 2 конфет.

Примеры:
Ввод: candyType = [1,1,2,2,3,3]
Вывод: 3

Ввод: candyType = [1,1,2,3]
Вывод: 2
'''

from typing import List

def distribute_candies(candyType: List[int]) -> int:
    unique_types = len(set(candyType))
    max_candies = len(candyType) // 2
    return min(unique_types, max_candies)