'''
You are given a string S and an array of strings words. All the words are of the same length.
A concatenated substring is a substring of S that consists of all the words in words concatenated together in any order, without any extra characters. Each word must appear exactly once.
Return a list of starting indices in S where such concatenated substrings begin. The order of the output does not matter.

Examples:
Input: S = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]

Input: S = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Input: S = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]

Дана строка S и массив строк words. Все слова в массиве имеют одинаковую длину.
Объединённая подстрока — это такая подстрока строки S, которая состоит из всех слов из массива words, соединённых друг с другом в любом порядке, без лишних символов.
Каждое слово должно встретиться ровно один раз.

Необходимо вернуть список начальных индексов таких объединённых подстрок в строке S.
Порядок индексов в ответе не имеет значения.

Примеры:
Вход: S = "barfoothefoobarman", words = ["foo", "bar"]
Выход: [0, 9]

Вход: S = "wordgoodgoodgoodbestword", words = ["word", "good", "best", "word"]
Выход: []

Вход: S = "barfoofoobarthefoobarman", words = ["bar", "foo", "the"]
Выход: [6, 9, 12]
'''

from typing import List
from collections import Counter

def find_substring(S: str, words: List[str]) -> List[int]:
    if not S or not words or not words[0]:
        return []

    word_length = len(words[0])
    word_count = len(words)
    total_length = word_length * word_count
    word_map = Counter(words)
    result = []

    for i in range(len(S) - total_length + 1):
        seen = {}
        for j in range(word_count):
            word_start = i + j * word_length
            word = S[word_start : word_start + word_length]
            if word not in word_map:
                break
            seen[word] = seen.get(word, 0) + 1
            if seen[word] > word_map[word]:
                break
        else:
            result.append(i)

    return result