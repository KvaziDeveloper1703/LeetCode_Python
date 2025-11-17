'''
You are given two strings, word_1 and word_2.

Create a new string by merging the two strings in an alternating pattern, starting with a character from word_1.

If one of the strings is longer than the other, append the remaining characters of the longer string at the end of the merged string.

Return the resulting merged string.

Examples:
Input: word_1 = "abc", word_2 = "pqr"
Output: "apbqcr"

Input: word_1 = "ab", word_2 = "pqrs"
Output: "apbqrs"

Даны две строки: word_1 и word_2.

Нужно создать новую строку, чередуя буквы из этих строк, начиная с буквы из word_1.

Если одна из строк длиннее другой, оставшиеся символы более длинной строки нужно дописать в конец результата.

Верните получившуюся объединённую строку.

Примеры:
Ввод: word_1 = "abc", word_2 = "pqr"
Вывод: "apbqcr"

Ввод: word_1 = "ab", word_2 = "pqrs"
Вывод: "apbqrs"
'''

def merge_alternately(word_1: str, word_2: str) -> str:
    result = []
    i = 0

    while i < len(word_1) or i < len(word_2):
        if i < len(word_1):
            result.append(word_1[i])
        if i < len(word_2):
            result.append(word_2[i])
        i += 1

    return "".join(result)