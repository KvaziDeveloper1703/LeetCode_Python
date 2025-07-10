'''
Given an array of integers citations, where citations[i] represents the number of citations a researcher received for their i‑th paper.

Return the h-index, which is defined as the maximum number h such that the researcher has at least h papers with at least h citations each.

Examples:
Input: citations = [3, 0, 6, 1, 5]
Output: 3

Input: citations = [1, 3, 1]
Output: 1

Дан массив целых чисел citations, где citations[i] — это количество цитирований, полученных исследователем за его i-ю статью.

Необходимо вернуть h-индекс — максимальное число h такое, что у исследователя есть как минимум h статей, каждая из которых была процитирована не менее чем h раз.

Примеры:
Ввод: citations = [3, 0, 6, 1, 5]
Вывод: 3

Ввод: citations = [1, 3, 1]
Вывод: 1
'''

from typing import List

def h_index(citations: List[int]) -> int:
    citations.sort(reverse=True)
    h_index = 0

    for i, citation in enumerate(citations):
        if citation >= i + 1:
            h_index = i + 1
        else:
            break

    return h_index