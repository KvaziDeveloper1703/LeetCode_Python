'''
Given two strings, S and T. String T is created by randomly shuffling the characters of string S and then adding one extra letter at a random position.

Return the letter that was added to T.

Examples:
Input: S = "abcd", T = "abcde"
Output: "e"

Input: S = "", T = "y"
Output: "y"

Даны две строки: S и T. Строка T получается из строки S путём случайной перестановки её символов и добавления одной дополнительной буквы в случайную позицию.

Верните букву, которая была добавлена в строку T.

Примеры:
Ввод: S = "abcd", T = "abcde"
Вывод: "e"

Ввод: S = "", T = "y"
Вывод: "y"
'''

def find_the_difference(S: str, T: str) -> str:
    result = 0

    for character in S:
        result ^= ord(character)

    for character in T:
        result ^= ord(character)

    return chr(result)