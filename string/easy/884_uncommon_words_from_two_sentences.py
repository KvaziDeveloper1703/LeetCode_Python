'''
A sentence is a string of words separated by single spaces, where each word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences and does not appear at all in the other.

Given two sentences sentence_1 and sentence_2, return a list of all uncommon words. You may return the answer in any order.

Examples:
Input: sentence_1 = "this apple is sweet", sentence_2 = "this apple is sour"
Output: ["sweet", "sour"]

Input: sentence_1 = "apple apple", sentence_2 = "banana"
Output: ["banana"]

Предложение — это строка, состоящая из слов, разделённых одиночными пробелами, где каждое слово состоит только из строчных букв.
Слово считается необычным, если оно встречается ровно один раз в одном из предложений и не встречается вообще в другом.

Даны два предложения sentence_1 и sentence_2. Верните список всех необычных слов. Порядок в списке может быть произвольным.

Примеры:
Ввод: sentence_1 = "this apple is sweet", sentence_2 = "this apple is sour"
Вывод: ["sweet", "sour"]

Ввод: sentence_1 = "apple apple", sentence_2 = "banana"
Вывод: ["banana"]
'''

from typing import List
from collections import Counter

def uncommon_from_sentences(sentence_1: str, sentence_2: str) -> List[str]:
    words_1 = sentence_1.split()
    words_2 = sentence_2.split()

    all_words = words_1 + words_2

    word_frequencies = Counter(all_words)

    uncommon_words = []
    for word, count in word_frequencies.items():
        if count == 1:
            uncommon_words.append(word)

    return uncommon_words