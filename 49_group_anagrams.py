'''
Given an array of strings given_strings, group the anagrams together. You can return the answer in any order.

Examples:
Input: given_strings = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: given_strings = [""]
Output: [[""]]

Input: given_strings = ["a"]
Output: [["a"]]

Дан массив строк given_strings. Необходимо сгруппировать анаграммы вместе.
Порядок групп в результате может быть любым.

Примеры:
Ввод: given_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
Вывод: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

Ввод: given_strings = [""]
Вывод: [[""]]

Ввод: given_strings = ["a"]
Вывод: [["a"]]
'''

from typing import List
from collections import defaultdict

def group_anagrams(given_strings: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)

    for word in given_strings:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)

    return list(anagrams.values())