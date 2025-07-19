'''
Given a string license_plate and an array of strings words.

Find the shortest completing word in words.

A completing word is a word that:
    + Contains all the letters in license_plate;
    + Letter matching is case-insensitive;
    + If a letter appears more than once in license_plate, it must appear at least that many times in the word.

Return the shortest word from words that satisfies the condition. If there are multiple shortest completing words, return the first one that appears in the array.

Examples:
Input: license_plate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"

Input: license_plate = "1s3 456", words = ["looks","pest","stew","show"]
Output: "pest"

Дан строковый параметр license_plate и массив строк words.

Нужно найти самое короткое завершающее слово из массива words.

Завершающее слово — это такое слово, которое:
    + Содержит все буквы, присутствующие в license_plate;
    + Сопоставление букв нечувствительно к регистру;
    + Если буква в license_plate встречается несколько раз, то и в слове она должна встречаться не реже.

Нужно вернуть самое короткое слово из words, удовлетворяющее этим условиям. Если таких слов несколько — вернуть первое, которое встречается в массиве.

Примеры:
Ввод: license_plate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Вывод: "steps"

Ввод: license_plate = "1s3 456", words = ["looks","pest","stew","show"]
Вывод: "pest"
'''

from typing import List
from collections import Counter

def shortest_completing_word(license_plate: str, words: List[str]) -> str:
    required = Counter(c.lower() for c in license_plate if c.isalpha())

    result = None
    for word in words:
        word_counter = Counter(word.lower())
        if all(word_counter[c] >= required[c] for c in required):
            if result is None or len(word) < len(result):
                result = word

    return result