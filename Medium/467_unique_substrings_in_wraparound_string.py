""" 
We define the string base as the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz". That is, it looks like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd..."

Given a string S, return the number of unique non-empty substrings of S that are present in the base string. A substring is considered present in base if it consists of consecutive characters in the alphabet, and it can wrap around from 'z' to 'a'.

Examples:
Input: S = "a"
Output: 1

Input: S = "cac"
Output: 2

Определим строку base как бесконечную циклическую строку "abcdefghijklmnopqrstuvwxyz". Она выглядит примерно так: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd..."

Дана строка S. Необходимо вернуть количество уникальных непустых подстрок строки S, которые содержатся в строке base. Подстрока считается допустимой, если её символы следуют в алфавитном порядке подряд, с возможностью перехода от 'z' к 'a'.

Примеры:
Ввод: S = "a"
Вывод: 1

Ввод: S = "cac"
Вывод: 2
"""

def find_substring_in_wrapround_string(S: str) -> int:
    if not S:
        return 0

    max_substring_length_ending_with = [0] * 26
    current_valid_length = 0

    for i in range(len(S)):
        if i > 0 and (ord(S[i]) - ord(S[i - 1]) == 1 or (S[i - 1] == 'z' and S[i] == 'a')):
            current_valid_length += 1
        else:
            current_valid_length = 1

        character_index = ord(S[i]) - ord('a')
        max_substring_length_ending_with[character_index] = max(
            max_substring_length_ending_with[character_index],
            current_valid_length
        )

    return sum(max_substring_length_ending_with)