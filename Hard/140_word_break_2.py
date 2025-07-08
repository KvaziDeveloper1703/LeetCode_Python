'''
Given a string S and a list of strings word_dict representing a dictionary, return all possible sentences where S is segmented into a sequence of valid dictionary words, with a space between each word.
You may reuse the same word from the dictionary multiple times.

Return the list of sentences in any order.

Example:
Input: S = "catsanddog", word_dict = ["cat", "cats", "and", "sand", "dog"]
Output: ["cats and dog", "cat sand dog"]

Дана строка S и список слов word_dict, представляющий словарь. Нужно вставить пробелы в строку S, чтобы получить все возможные предложения, состоящие только из слов из словаря.
Можно использовать одно и то же слово из словаря неограниченное количество раз.

Верните все возможные предложения в произвольном порядке.

Пример:
Вход: S = "catsanddog", word_dict = ["cat", "cats", "and", "sand", "dog"]
Выход: ["cats and dog", "cat sand dog"]
'''

from typing import List

def word_break(S: str, word_dict: List[str]) -> List[str]:
    word_set = set(word_dict)
    memo = {}

    def backtrack(start: int) -> List[str]:
        if start in memo:
            return memo[start]
        if start == len(S):
            return [""]

        sentences = []
        for end in range(start + 1, len(S) + 1):
            word = S[start:end]
            if word in word_set:
                rest_sentences = backtrack(end)
                for sentence in rest_sentences:
                    if sentence:
                        sentences.append(word + " " + sentence)
                    else:
                        sentences.append(word)
        memo[start] = sentences
        return sentences
    return backtrack(0)