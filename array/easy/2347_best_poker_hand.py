'''
You are given two arrays: an integer array ranks and a character array suits.

There are 5 cards, where the i-th card has a rank ranks[i] and a suit suits[i].

You need to determine the best possible poker hand that can be formed from these cards.

The possible poker hands are listed below from best to worst:
    - "Flush" - all five cards have the same suit;
    - "Three of a Kind" - three cards have the same rank;
    - "Pair" - two cards have the same rank;
    - "High Card" - any single card.

Return a string representing the best poker hand that can be made from the given cards.

Examples:
Input: ranks = [13, 2, 3, 1, 9], suits = ["a", "a", "a", "a", "a"]
Output: "Flush"

Input: ranks = [4, 4, 2, 4, 4], suits = ["d", "a", "a", "b", "c"]
Output: "Three of a Kind"

Вам даны два массива: целочисленный массив ranks и символьный массив suits.

Имеется 5 карт, где i-я карта имеет ранг ranks[i] и масть suits[i].

Необходимо определить лучшую возможную покерную комбинацию, которую можно составить из этих карт.

Возможные комбинации приведены ниже от лучшей к худшей:
    - "Flush" - все пять карт одной масти;
    - "Three of a Kind" - три карты одного ранга;
    - "Pair" - две карты одного ранга;
    - "High Card" - одиночная карта.

Верните строку, представляющую лучшую покерную комбинацию, которую можно получить из данных карт.

Примеры:
Ввод: ranks = [13, 2, 3, 1, 9], suits = ["a", "a", "a", "a", "a"]
Вывод: "Flush"

Ввод: ranks = [4, 4, 2, 4, 4], suits = ["d", "a", "a", "b", "c"]
Вывод: "Three of a Kind"
'''

from typing import List
from collections import Counter

def best_hand(ranks: List[int], suits: List[str]) -> str:
    if len(set(suits)) == 1:
        return "Flush"

    max_same_rank = max(Counter(ranks).values())

    if max_same_rank >= 3:
        return "Three of a Kind"
    elif max_same_rank == 2:
        return "Pair"
    else:
        return "High Card"