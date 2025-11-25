'''
A fancy string is a string in which no three consecutive characters are the same.

You are given a string s. Delete the minimum number of characters from s so that it becomes a fancy string.

Return the resulting string after the deletions. It can be shown that the answer is always unique.

Examples:
Input: s = "leeetcode"
Output: "leetcode"

Input: s = "aaabaaaa"
Output: "aabaa"

Красивой строкой называется строка, в которой нет трёх подряд одинаковых символов.

Дана строка s. Нужно удалить минимальное количество символов из s, чтобы она стала красивой.

Верните получившуюся строку после всех удалений. Гарантируется, что ответ всегда однозначен.

Примеры:
Ввод: s = "leeetcode"
Вывод: "leetcode"

Ввод: s = "aaabaaaa"
Вывод: "aabaa"
'''

def make_fancy_string(s: str) -> str:
    result_characters = []
    consecutive_count = 0
    previous_character = ""

    for character in s:
        if character == previous_character:
            consecutive_count += 1
        else:
            consecutive_count = 1
            previous_character = character

        if consecutive_count <= 2:
            result_characters.append(character)

    return "".join(result_characters)