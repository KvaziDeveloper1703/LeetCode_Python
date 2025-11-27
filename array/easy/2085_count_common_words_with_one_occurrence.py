'''
You are given two string arrays, words_1 and words_2.

Return the number of strings that appear exactly once in each of the two arrays.

Examples:
Input: words_1 = ["leetcode","is","amazing","as","is"], words_2 = ["amazing","leetcode","is"]
Output: 2

Input: words_1 = ["b","bb","bbb"], words_2 = ["a","aa","aaa"]
Output: 0

Даны два массива строк: words_1 и words_2.

Нужно вернуть количество строк, которые встречаются ровно один раз в каждом из этих двух массивов.

Примеры:
Ввод: words_1 = ["leetcode","is","amazing","as","is"], words_2 = ["amazing","leetcode","is"]
Вывод: 2

Ввод: words_1 = ["b","bb","bbb"], words_2 = ["a","aa","aaa"]
Вывод: 0
'''

from typing import List

def count_words(words_1: List[str], words_2: List[str]) -> int:
    frequency_words_1 = {}
    frequency_words_2 = {}

    for word in words_1:
        frequency_words_1[word] = frequency_words_1.get(word, 0) + 1

    for word in words_2:
        frequency_words_2[word] = frequency_words_2.get(word, 0) + 1

    matching_words_count = 0

    for word in frequency_words_1:
        if frequency_words_1.get(word, 0) == 1 and frequency_words_2.get(word, 0) == 1:
            matching_words_count += 1

    return matching_words_count