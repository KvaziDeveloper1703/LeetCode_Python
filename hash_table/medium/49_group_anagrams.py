'''
Given an array of strings named strings, group the anagrams together. You can return the answer in any order.

Examples:
Input: strings = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strings = [""]
Output: [[""]]

Дан массив строк strings. Необходимо сгруппировать анаграммы вместе.
Порядок групп в результате может быть любым.

Примеры:
Ввод: strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
Вывод: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

Ввод: strings = [""]
Вывод: [[""]]
'''

from typing import List
from collections import defaultdict

def group_anagrams(strings: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)

    for word in strings:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)

    return list(anagrams.values())