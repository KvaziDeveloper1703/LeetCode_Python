'''
Given a string text and two words: first and second.

We are looking for occurrences in text of the form: first second third, where:
    + second comes immediately after first;
    + third comes immediately after second.

Return an array of all words third that follow each occurrence of "first second" in the text.

Examples:
Input:  text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl", "student"]

Input:  text = "we will we will rock you", first = "we", second = "will"
Output: ["we", "rock"]

Дана строка text и два слова: first и second.

Нужно найти все вхождения в тексте последовательности: first second third, где:
    + second идёт сразу после first;
    + third идёт сразу после second.

Верните массив всех слов third, которые следуют за каждой парой "first second" в тексте.

Примеры:
Ввод:  text = "alice is a good girl she is a good student", first = "a", second = "good"
Вывод: ["girl", "student"]

Ввод:  text = "we will we will rock you", first = "we", second = "will"
Вывод: ["we", "rock"]
'''

from typing import List

def find_ocurrences(text: str, first: str, second: str) -> List[str]:
    words = text.split()
    result = []

    for i in range(len(words) - 2):
        if words[i] == first and words[i + 1] == second:
            result.append(words[i + 2])
    return result