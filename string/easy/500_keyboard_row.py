'''
Given an array of strings words, return the words that can be typed using letters of the alphabet from only one row of the American keyboard.
Note that the strings are case-insensitive, meaning both lowercase and uppercase versions of the same letter are treated as being on the same keyboard row.

On the American keyboard:
    + The first row consists of the characters: "qwertyuiop";
    + The second row consists of the characters: "asdfghjkl";
    + The third row consists of the characters: "zxcvbnm".

Examples:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Input: words = ["omk"]
Output: []

Дан массив строк words. Верните те слова из массива, которые можно напечатать, используя буквы только из одной строки американской клавиатуры.
Учтите, что регистр букв не имеет значения: строчные и заглавные буквы считаются находящимися в одной строке клавиатуры.

На американской клавиатуре:
    + Первая строка содержит символы: "qwertyuiop";
    + Вторая строка содержит символы: "asdfghjkl";
    + Третья строка содержит символы: "zxcvbnm".

Примеры:
Ввод: words = ["Hello","Alaska","Dad","Peace"]
Вывод: ["Alaska","Dad"]

Ввод: words = ["omk"]
Вывод: []
'''

from typing import List

def find_words(words: List[str]) -> List[str]:
    rows = [
        set("qwertyuiop"),
        set("asdfghjkl"),
        set("zxcvbnm")
    ]

    result = []
    for word in words:
        lower_word = set(word.lower())
        if any(lower_word <= row for row in rows):
            result.append(word)
    return result