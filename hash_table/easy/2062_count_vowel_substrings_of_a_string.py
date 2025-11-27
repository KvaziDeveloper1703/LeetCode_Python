'''
A substring is a contiguous and non-empty sequence of characters within a string.

A vowel substring is a substring that:
    - contains only vowels ('a', 'e', 'i', 'o', 'u'), and
    - includes all five vowels at least once.

Given a string word, return the number of vowel substrings in it.

Examples:
Input: word = "aeiouu"
Output: 2

Input: word = "unicornarihan"
Output: 0

Подстрока - это непрерывная последовательность символов внутри строки.

Гласная подстрока - это подстрока, которая:
    - состоит только из гласных ('a', 'e', 'i', 'o', 'u'), и
    - содержит все пять гласных хотя бы один раз.

По заданной строке word нужно вернуть количество гласных подстрок.

Примеры:
Ввод: word = "aeiouu"
Вывод: 2

Ввод: word = "unicornarihan"
Вывод: 0
'''

def count_vowel_substrings(word: str) -> int:
    vowel_characters = {"a", "e", "i", "o", "u"}
    vowel_substrings_count = 0
    word_length = len(word)

    for start_index in range(word_length):
        used_vowel_characters = set()
        for end_index in range(start_index, word_length):
            current_character = word[end_index]
            if current_character not in vowel_characters:
                break
            used_vowel_characters.add(current_character)
            if len(used_vowel_characters) == 5:
                vowel_substrings_count += 1

    return vowel_substrings_count