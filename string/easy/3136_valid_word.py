'''
A word is considered valid if:
    - It contains at least 3 characters;
    - It contains only digits and English letters;
    - It contains at least one vowel;
    - It contains at least one consonant.

You are given a string word.

Return True if word is valid, otherwise return False.

Examples:
Input: word = "234Adas"
Output: True

Input: word = "b3"
Output: False

Слово считается корректным, если:
    - Оно содержит минимум 3 символа;
    - Оно состоит только из цифр и английских букв;
    - В слове есть хотя бы одна гласная буква;
    - В слове есть хотя бы одна согласная буква.

Дана строка word.

Верни True, если word является корректным, иначе верни False.

Примеры:
Ввод: word = "234Adas"
Вывод: True

Ввод: word = "b3"
Вывод: false
'''

def is_valid(word: str) -> bool:
    if len(word) < 3:
        return False

    vowels = set("aeiouAEIOU")
    has_vowel = False
    has_consonant = False

    for character in word:
        if not character.isalnum():
            return False

        if character.isalpha():
            if character in vowels:
                has_vowel = True
            else:
                has_consonant = True

    return has_vowel and has_consonant