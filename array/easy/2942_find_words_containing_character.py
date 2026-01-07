'''
You are given a 0-indexed array of strings called words and a character x.

Your task is to find all indices of the words in the array that contain the character x at least once.

Return an array of these indices. The indices may be returned in any order.

Examples:
Input: words = ["leet", "code"], x = "e"
Output: [0, 1]

Input: words = ["abc", "bcd", "aaaa", "cbc"], x = "a"
Output: [0, 2]

Дан массив строк words с индексацией с нуля и символ x.

Необходимо найти все индексы слов из массива, которые содержат символ x хотя бы один раз.

Верните массив этих индексов. Порядок индексов может быть произвольным.

Примеры:
Ввод: words = ["leet", "code"], x = "e"
Вывод: [0, 1]

Ввод: words = ["abc", "bcd", "aaaa", "cbc"], x = "a"
Вывод: [0, 2]
'''

from typing import List

def find_words_containing(words: List[str], x: str) -> List[int]:
    indices = []

    for index in range(len(words)):
        if x in words[index]:
            indices.append(index)

    return indices