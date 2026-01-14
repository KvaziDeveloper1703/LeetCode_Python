'''
You are given a string word.
A letter is called special if it appears in word both in lowercase and in uppercase.

Return the number of special letters in word.

Examples:
Input: word = "aaAbcBC"
Output: 3

Input: word = "abc"
Output: 0

Дана строка word.
Буква называется особой, если она встречается в строке и в нижнем регистре, и в верхнем регистре.

Верни количество особых букв в строке word.

Примеры:
Ввод: word = "aaAbcBC"
Вывод: 3

Ввод: word = "abc"
Вывод: 0
'''

def number_of_special_chars(word: str) -> int:
    unique_characters = set(word)
    special_letters_count = 0

    for character in unique_characters:
        if character.islower() and character.upper() in unique_characters:
            special_letters_count += 1

    return special_letters_count