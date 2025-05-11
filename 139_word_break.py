'''
Given a string S and a list of strings word_dict representing a dictionary, return true if S can be segmented into a space-separated sequence of one or more words from the dictionary.
You may reuse the same word from the dictionary multiple times in the segmentation.

Examples:
Input: S = "leetcode", word_dict = ["leet", "code"]
Output: true

Input: S = "applepenapple", word_dict = ["apple", "pen"]
Output: true

Дана строка S и список строк word_dict, представляющий словарь. Верните true, если строку S можно разбить на последовательность слов из словаря, разделённых пробелами.
Разрешается многократно использовать одни и те же слова из словаря.

Примеры:
Вход: S = "leetcode", word_dict = ["leet", "code"]
Выход: true

Вход: S = "applepenapple", word_dict = ["apple", "pen"]
Выход: true
'''

from typing import List

def word_break(input_string: str, dictionary_words: List[str]) -> bool:
    word_set = set(dictionary_words)
    can_be_segmented = [False] * (len(input_string) + 1)
    can_be_segmented[0] = True

    for end_index in range(1, len(input_string) + 1):
        for start_index in range(end_index):
            word = input_string[start_index:end_index]
            if can_be_segmented[start_index] and word in word_set:
                can_be_segmented[end_index] = True
                break

    return can_be_segmented[len(input_string)]