'''
A sentence is defined as a list of words separated by a single space, with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] is one complete sentence.

Your task is to return the maximum number of words found in any single sentence.

Examples:
Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6

Input: sentences = ["please wait", "continue to fight", "continue to win"]
Output: 3

Предложение - это последовательность слов, разделённых одним пробелом, без пробелов в начале или конце.

Вам дан массив строк sentences, где каждый элемент sentences[i] представляет собой одно предложение.

Ваша задача - вернуть максимальное число слов, которое встречается в каком-либо предложении из массива.

Примеры:
Ввод: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Вывод: 6

Ввод: sentences = ["please wait", "continue to fight", "continue to win"]
Вывод: 3
'''

from typing import List

def most_words_found(sentences: List[str]) -> int:
    maximum_word_count = 0

    for sentence in sentences:
        number_of_words = len(sentence.split(" "))
        if number_of_words > maximum_word_count:
            maximum_word_count = number_of_words

    return maximum_word_count