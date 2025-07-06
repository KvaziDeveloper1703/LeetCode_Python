"""
You are given two strings: ransom_note and magazine. Return true if the ransom_note can be constructed using the letters from magazine, and false otherwise.
Each letter in magazine can only be used once in ransom_note.

Examples:
Input: ransom_note = "a", magazine = "b"
Output: false

Input: ransom_note = "aa", magazine = "ab"
Output: false

Даны две строки: ransom_note и magazine. Необходимо вернуть true, если строку ransom_note можно составить из букв строки magazine, и false — в противном случае.
Каждую букву из строки magazine можно использовать только один раз при составлении ransom_note.

Примеры:
Ввод: ransom_note = "a", magazine = "b"
Вывод: false

Ввод: ransom_note = "aa", magazine = "ab"
Вывод: false
"""

from collections import Counter

def can_construct(ransom_note: str, magazine: str) -> bool:
    ransom_note_character_counts = Counter(ransom_note)
    magazine_character_counts = Counter(magazine)

    for character, required_count in ransom_note_character_counts.items():
        if magazine_character_counts[character] < required_count:
            return False

    return True