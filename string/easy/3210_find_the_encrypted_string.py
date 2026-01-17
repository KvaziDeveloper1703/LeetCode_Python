'''
You are given a string s and an integer k. Encrypt the string using the following rule: For every character c in s, replace it with the character that is k positions after c in the string s, moving cyclically.
Return the resulting encrypted string.

Examples:
Input: s = "dart", k = 3
Output: "tdar"

Input: s = "aaa", k = 1
Output: "aaa"

Дана строка s и целое число k. Нужно зашифровать строку по следующему алгоритму: Для каждого символа c в строке s заменить его на символ, который находится на k позиций правее него в строке s, при этом переход выполняется циклически.
Верните полученную зашифрованную строку.

Примеры:
Ввод: s = "dart", k = 3
Вывод: "tdar"

Ввод: s = "aaa", k = 1
Вывод: "aaa"
'''

def get_encrypted_string(s: str, k: int) -> str:
    stringLength = len(s)
    encryptedCharacters = []

    for index in range(stringLength):
        newIndex = (index + k) % stringLength
        encryptedCharacters.append(s[newIndex])

    return "".join(encryptedCharacters)