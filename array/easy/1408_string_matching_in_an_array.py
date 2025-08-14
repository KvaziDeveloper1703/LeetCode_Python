'''
Given an array of strings words.

Return all strings in words that are a substring of another string in the same array. The answer can be returned in any order.

Examples:
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]

Input: words = ["leetcode","et","code"]
Output: ["et","code"]

Дан массив строк words.

Верните все строки из words, которые являются подстроками другой строки в этом же массиве. Ответ можно вернуть в любом порядке.

Примеры:
Ввод: words = ["mass","as","hero","superhero"]
Вывод: ["as","hero"]

Ввод: words = ["leetcode","et","code"]
Вывод: ["et","code"]
'''

from typing import List

def string_matching(words: List[str]) -> List[str]:
    result = []
    n = len(words)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if words[i] in words[j]:
                result.append(words[i])
                break
    return result