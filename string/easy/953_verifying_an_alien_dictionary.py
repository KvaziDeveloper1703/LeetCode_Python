'''
In an alien language, they surprisingly use English lowercase letters, but possibly in a different order. The order of the alphabet is given as a permutation of all 26 lowercase English letters.

Given a list of words written in this alien language and the custom alphabet order.

Your task is to determine if the words are sorted lexicographically according to the rules of this alien language.

Return True if the words are sorted, and False otherwise.

Examples:
Input: words = ["hello", "leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: True

Input: words = ["word", "world", "row"], order = "worldabcefghijkmnpqstuvxyz"
Output: False

В одном инопланетном языке, как ни странно, также используются английские строчные буквы, но в другом порядке. Порядок алфавита задаётся в виде перестановки из 26 строчных английских букв.

Вам дан список слов, записанных на этом инопланетном языке, и порядок букв в алфавите.

Ваша задача — проверить, отсортированы ли слова лексикографически в соответствии с этим алфавитом.

Верните True, если слова отсортированы, и False — если нет.

Примеры:
Ввод: words = ["hello", "leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Вывод: True

Ввод: words = ["word", "world", "row"], order = "worldabcefghijkmnpqstuvxyz"
Вывод: False
'''

from typing import List

def is_alien_sorted(words: List[str], order: str) -> bool:
    character_priority = {character: position for position, character in enumerate(order)}

    def is_order_preserved(previous_word: str, next_word: str) -> bool:
        for previous_char, next_char in zip(previous_word, next_word):
            if character_priority[previous_char] < character_priority[next_char]:
                return True
            elif character_priority[previous_char] > character_priority[next_char]:
                return False
        return len(previous_word) <= len(next_word)

    for word_index in range(len(words) - 1):
        if not is_order_preserved(words[word_index], words[word_index + 1]):
            return False

    return True