'''
Given a string s, find the maximum length of a substring such that each character appears at most two times in that substring.
Return the maximum possible length.

Examples:
Input: s = "bcbbbcba"
Output: 4

Input: s = "aaaa"
Output: 2

Дана строка s. Необходимо найти максимальную длину подстроки, в которой каждый символ встречается не более двух раз.
Верните максимально возможную длину такой подстроки.

Примеры:
Ввод: s = "bcbbbcba"
Вывод: 4

Ввод: s = "aaaa"
Вывод: 2
'''

def maximum_length_substring(s: str) -> int:
    left_index = 0
    character_counts = {}
    maximum_length = 0

    for right_index in range(len(s)):
        current_character = s[right_index]
        character_counts[current_character] = character_counts.get(current_character, 0) + 1

        while character_counts[current_character] > 2:
            left_character = s[left_index]
            character_counts[left_character] -= 1
            left_index += 1

        current_length = right_index - left_index + 1
        if current_length > maximum_length:
            maximum_length = current_length

    return maximum_length