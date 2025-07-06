'''
You are given a string S. Your task is to find the length of the longest substring that contains no duplicate characters.
A substring is a contiguous sequence of characters within the string.

Examples:
Input: S = "abcabcbb"
Output: 3

Input: S = "bbbbb"
Output: 1

Input: S = "pwwkew"
Output: 3

Дана строка S. Ваша задача — найти длину самой длинной подстроки, не содержащей повторяющихся символов.
Подстрока — это непрерывная последовательность символов внутри строки.

Примеры:
Ввод: S = "abcabcbb"
Вывод: 3

Ввод: S = "bbbbb"
Вывод: 1

Ввод: S = "pwwkew"
Вывод: 3
'''

def length_of_longest_substring(S: str) -> int:
        character_set = set()
        left = 0
        max_length = 0

        for right in range(len(S)):
            while S[right] in character_set:
                character_set.remove(S[left])
                left += 1
            character_set.add(S[right])
            max_length = max(max_length, right - left + 1)

        return max_length