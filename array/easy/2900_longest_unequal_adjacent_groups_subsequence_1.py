'''
You are given a string array words and a binary array groups, both of length n.

A subsequence of words is called alternating if, for every pair of consecutive strings in the subsequence, the corresponding values in groups are different.

In other words, the subsequence must not contain two consecutive elements whose group values are both 0 or both 1.

Your task is to select the longest alternating subsequence from the array words.

Return the selected subsequence.

If there are multiple valid answers, return any of them.

Examples:
Input: words = ["e","a","b"], groups = [0,0,1]
Output: ["e","b"]

Input: words = ["a","b","c","d"], groups = [1,0,1,1]
Output: ["a","b","c"]

Вам дан массив строк words и бинарный массив groups, оба длины n.

Подпоследовательность массива words называется чередующейся, если для любых двух соседних строк в подпоследовательности соответствующие значения в массиве groups различны.

Иными словами, в подпоследовательности не может быть двух подряд идущих элементов с одинаковым значением 0 или 1 в массиве groups.

Ваша задача - выбрать самую длинную чередующуюся подпоследовательность из массива words.

Верните выбранную подпоследовательность.

Если существует несколько корректных решений, верните любое из них.

Примеры:
Ввод: words = ["e","a","b"], groups = [0,0,1]
Вывод: ["e","b"]

Ввод: words = ["a","b","c","d"], groups = [1,0,1,1]
Вывод: ["a","b","c"]
'''

from typing import List

def get_longest_subsequence(words: List[str], groups: List[int]) -> List[str]:
    longest_subsequence = [words[0]]
    last_group_value = groups[0]

    for index in range(1, len(words)):
        if groups[index] != last_group_value:
            longest_subsequence.append(words[index])
            last_group_value = groups[index]

    return longest_subsequence