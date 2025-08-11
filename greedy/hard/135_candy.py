'''
There are N children standing in a line, and each child has a rating represented by the integer array ratings.
You need to distribute candies to these children based on the following rules:
    + Every child must receive at least one candy;
    + A child with a higher rating than an immediate neighbor must receive more candies than that neighbor.

Your task is to determine the minimum number of candies needed to distribute to all the children while satisfying these rules.

Examples:
Input: ratings = [1, 0, 2]
Output: 5

Input: ratings = [1, 2, 2]
Output: 4

Есть N детей, стоящих в ряд, и у каждого ребёнка есть рейтинг, представленный массивом целых чисел ratings.
Вам нужно раздать конфеты детям в соответствии со следующими правилами:
    + Каждый ребёнок должен получить как минимум одну конфету;
    + Ребёнок с более высоким рейтингом, чем его сосед, должен получить больше конфет, чем этот сосед.

Ваша задача — определить минимальное количество конфет, которое нужно раздать всем детям, чтобы соблюсти указанные правила.

Примеры:
Ввод: ratings = [1, 0, 2]
Вывод: 5

Ввод: ratings = [1, 2, 2]
Вывод: 4
'''

from typing import List

def distribute_candies(ratings: List[int]) -> int:
    number_of_children = len(ratings)
    candies = [1] * number_of_children

    for i in range(1, number_of_children):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    for i in range(number_of_children - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)