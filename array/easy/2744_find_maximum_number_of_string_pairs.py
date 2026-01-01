'''
You are given a 0-indexed array words consisting of distinct strings.

Two strings words[i] and words[j] can be paired if all of the following conditions are met:
    - words[i] is equal to the reverse of words[j];
    - 0 ≤ i < j < words.length.

Each string can be used in at most one pair.

Return the maximum number of pairs that can be formed from the array words.

Examples:
Input: words = ["cd", "ac", "dc", "ca", "zz"]
Output: 2

Input: words = ["ab", "ba", "cc"]
Output: 1

Дан 0-индексированный массив words, состоящий из уникальных строк.

Две строки words[i] и words[j] можно объединить в пару, если выполняются все условия:
    - строка words[i] равна обратной строке words[j];
    - 0 ≤ i < j < words.length.

Каждая строка может входить не более чем в одну пару.

Верните максимальное количество пар, которое можно составить из массива words.

Примеры:
Ввод: words = ["cd", "ac", "dc", "ca", "zz"]
Вывод: 2

Ввод: words = ["ab", "ba", "cc"]
Вывод: 1
'''

from typing import List

def maximum_number_of_string_pairs(words: List[str]) -> int:
    seen_words = set()
    number_of_pairs = 0

    for current_word in words:
        reversed_word = current_word[::-1]

        if reversed_word in seen_words:
            number_of_pairs += 1
        else:
            seen_words.add(current_word)

    return number_of_pairs