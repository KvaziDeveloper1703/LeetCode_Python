'''
Given a string array words.

Return the maximum value of length(word[i]) * length(word[j]) where the two words do not share any common letters.
If no such pair of words exists, return 0.

Examples:
Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16

Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4

Дан массив строк words.

Верните максимальное значение length(word[i]) * length(word[j]) для таких двух слов, которые не имеют общих букв.
Если таких пар слов не существует, верните 0.

Примеры:
Ввод: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Вывод: 16

Ввод: words = ["a","ab","abc","d","cd","bcd","abcd"]
Вывод: 4
'''

from typing import List

def max_product(words: List[str]) -> int:
    n = len(words)
    masks = [0] * n
    lengths = [len(word) for word in words]

    for i, word in enumerate(words):
        mask = 0
        for char in word:
            mask |= 1 << (ord(char) - ord('a'))
        masks[i] = mask

    max_product = 0

    for i in range(n):
        for j in range(i + 1, n):
            if masks[i] & masks[j] == 0:
                max_product = max(max_product, lengths[i] * lengths[j])

    return max_product