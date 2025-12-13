'''
You are given two 0-indexed strings s and target. You may take any characters from s and rearrange them to form new strings.

Return the maximum number of copies of target that can be formed using the characters from s.

Examples:
Input: s = "ilovecodingonleetcode", target = "code"
Output: 2

Input: s = "abcba", target = "abc"
Output: 1

Вам даны две строки с нулевой индексацией s и target. Вы можете брать любые символы из строки s и переставлять их, чтобы формировать новые строки.

Необходимо вернуть максимальное количество копий строки target, которые можно составить из символов строки s.

Примеры:
Ввод: s = "ilovecodingonleetcode", target = "code"
Вывод: 2

Ввод: s = "abcba", target = "abc"
Вывод: 1
'''

from collections import Counter

def rearrange_сharacters(source_string: str, target_string: str) -> int:
    source_character_counts = Counter(source_string)
    target_character_counts = Counter(target_string)

    maximum_copies = float('inf')

    for character in target_character_counts:
        available_copies = (source_character_counts[character]// target_character_counts[character])
        maximum_copies = min(maximum_copies, available_copies)

    return maximum_copies