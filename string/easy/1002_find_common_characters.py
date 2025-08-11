'''
Given a string array words.

Return an array of all characters that appear in every string in words, including duplicates. You may return the answer in any order.

Examples:
Input: words = ["bella", "label", "roller"]
Output: ["e", "l", "l"]

Input: words = ["cool", "lock", "cook"]
Output: ["c", "o"]

Дан массив строк words.

Верните массив всех символов, которые встречаются во всех строках массива words, включая повторяющиеся. Ответ можно вернуть в любом порядке.

Примеры:
Ввод: words = ["bella", "label", "roller"]
Вывод: ["e", "l", "l"]

Ввод: words = ["cool", "lock", "cook"]
Вывод: ["c", "o"]
'''

from typing import List
from collections import Counter

def common_characters(words: List[str]) -> List[str]:
    common = Counter(words[0])
    for word in words[1:]:
        common &= Counter(word)
    result = []
    for char, count in common.items():
        result.extend([char] * count)
    return result