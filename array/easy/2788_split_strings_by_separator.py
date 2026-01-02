'''
You are given an array of strings words and a character separator.

For each string in words, split it using the given separator.

Return an array of strings containing all the substrings obtained after splitting, excluding empty strings.

Examples:
Input: words = ["one.two.three", "four.five", "six"], separator = "."
Output: ["one", "two", "three", "four", "five", "six"]

Input: words = ["$easy$", "$problem$"], separator = "$"
Output: ["easy", "problem"]

Вам дан массив строк words и символ-разделитель separator.

Для каждой строки в массиве words необходимо выполнить разбиение по символу separator.

Верните массив строк, содержащий все подстроки, полученные после разбиения, исключая пустые строки.

Примеры:
Ввод: words = ["one.two.three", "four.five", "six"], separator = "."
Вывод: ["one", "two", "three", "four", "five", "six"]

Ввод: words = ["$easy$", "$problem$"], separator = "$"
Вывод: ["easy", "problem"]
'''

from typing import List

def split_words_by_separator(words: List[str], separator: str) -> List[str]:
    result = []

    for word in words:
        parts = word.split(separator)
        for part in parts:
            if part:
                result.append(part)

    return result