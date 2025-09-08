'''
Given a string text consisting of words separated by spaces.
    + Each word consists of one or more lowercase English letters;
    + Words are separated by at least one space;
    + It is guaranteed that text contains at least one word.

Rearrange the spaces so that:
    1) There is an equal number of spaces between every pair of adjacent words, and this number is maximized;
    2) If the spaces cannot be evenly redistributed, place the extra spaces at the end.

The returned string must have the same length as the original text.

Examples:
Input: text = "  this   is  a sentence "
Output: "this   is   a   sentence"

Input: text = " practice   makes   perfect"
Output: "practice   makes   perfect "

Дана строка text, состоящая из слов и пробелов.
    + Каждое слово состоит из одной или более строчных букв английского алфавита;
    + Слова разделены хотя бы одним пробелом;
    + Гарантируется, что строка содержит хотя бы одно слово.

Нужно переставить пробелы так, чтобы:
1) Между каждой парой соседних слов было одинаковое количество пробелов, и это количество было максимально возможным;
2) Если все пробелы не удаётся распределить равномерно, оставшиеся пробелы добавляются в конец строки.

Возвращаемая строка должна иметь ту же длину, что и исходная text.

Примеры:
Ввод: text = "  this   is  a sentence "
Вывод: "this   is   a   sentence"

Ввод: text = " practice   makes   perfect"
Вывод: "practice   makes   perfect "
'''

def reorder_spaces(text: str) -> str:
    spaces = text.count(" ")
    words = text.split()

    if len(words) == 1:
        return words[0] + " " * spaces

    gaps = len(words) - 1
    space_between = spaces // gaps
    extra_spaces = spaces % gaps

    return (" " * space_between).join(words) + " " * extra_spaces