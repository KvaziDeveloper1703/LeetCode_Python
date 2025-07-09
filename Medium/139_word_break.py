'''
Given a string S and a list of strings dictionary_of_words representing a dictionary.

Return True if S can be segmented into a space-separated sequence of one or more words from the dictionary. You may reuse the same word from the dictionary multiple times in the segmentation.

Examples:
Input: S = "leetcode", dictionary_of_words = ["leet", "code"]
Output: True

Input: S = "applepenapple", dictionary_of_words = ["apple", "pen"]
Output: True

Дана строка S и список строк dictionary_of_words, представляющий словарь. Верните True, если строку S можно разбить на последовательность слов из словаря, разделённых пробелами.
Разрешается многократно использовать одни и те же слова из словаря.

Примеры:
Ввод: S = "leetcode", dictionary_of_words = ["leet", "code"]
Вывод: True

Ввод: S = "applepenapple", dictionary_of_words = ["apple", "pen"]
Вывод: True
'''

from typing import List

def word_break(S: str, dictionary_of_words: List[str]) -> bool:
    set_of_words = set(dictionary_of_words)
    can_be_segmented = [False] * (len(S) + 1)
    can_be_segmented[0] = True

    for end_index in range(1, len(S) + 1):
        for start_index in range(end_index):
            word = S[start_index:end_index]
            if can_be_segmented[start_index] and word in set_of_words:
                can_be_segmented[end_index] = True
                break

    return can_be_segmented[len(S)]