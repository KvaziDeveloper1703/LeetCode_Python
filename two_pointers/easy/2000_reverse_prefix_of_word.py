'''
You are given a 0-indexed string word and a character ch.
Reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch.
If ch does not appear in word, do nothing.

For example, if word = "abcdefd" and ch = "d", you reverse the segment from index 0 to 3, resulting in "dcbaefd".

Return the resulting string.

Examples:
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"

Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"

Дана строка word, индексируемая с нуля, и символ ch.
Нужно развернуть часть строки word, которая начинается с индекса 0 и заканчивается индексом первого вхождения символа ch.
Если символ ch не встречается в строке, ничего делать не нужно.

Например, если word = "abcdefd" и ch = "d", разворачиваем участок с 0 по 3, получаем "dcbaefd".

Верните получившуюся строку.

Примеры:
Ввод: word = "abcdefd", ch = "d"
Вывод: "dcbaefd"

Ввод: word = "xyxzxe", ch = "z"
Вывод: "zxyxxe"
'''

def reverse_prefix(word: str, ch: str) -> str:
    first_occurrence_index = word.find(ch)

    if first_occurrence_index == -1:
        return word

    reversed_prefix = word[:first_occurrence_index + 1][::-1]
    remaining_part = word[first_occurrence_index + 1:]
        
    return reversed_prefix + remaining_part