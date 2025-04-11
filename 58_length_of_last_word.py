'''
Given a string S containing words and spaces, return the length of the last word in the string.
A word is defined as the longest sequence of non-space characters.

Example:
Input: S = "Hello World"
Output: 5

Дана строка S, содержащая слова и пробелы. Верните длину последнего слова в строке.
Словом считается самая длинная последовательность символов, не содержащих пробелов.

Пример:
Вход: S = "Hello World"
Выход: 5
'''

def length_of_last_word(S: str) -> int:
    return len(S.strip().split()[-1])