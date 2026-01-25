"""
Alice and Bob are playing a game. At the beginning, Alice has a string: word = "a".

You are given a positive integer k.

Bob asks Alice to repeat the following operation forever:
    - Create a new string by changing every character in word to the next character in the English alphabet;
    - Append this new string to the end of the original word.

Your task is to return the k-th character of word, after performing enough operations so that the length of word becomes at least k.

Examples:
Input: k = 5
Output: "b"

Input: k = 10
Output: "c"

Алиса и Боб играют в игру. Изначально у Алисы есть строка: word = "a".

Вам дано положительное целое число k.

Боб просит Алису бесконечно повторять следующую операцию:
    - Создать новую строку, заменив каждый символ в word на следующий символ английского алфавита;
    - Приписать полученную строку в конец исходной word.

Ваша задача - вернуть k-й символ строки word, после того как будет выполнено достаточно операций, чтобы длина строки стала не меньше k.

Примеры:
Ввод: k = 5
Вывод: "b"

Ввод: k = 10
Вывод: "c"
"""

def kth_character(k: int) -> str:
    shift = 0

    while k > 1:
        length = 1
        while length * 2 < k:
            length *= 2

        if k > length:
            k -= length
            shift += 1

    return chr(ord('a') + (shift % 26))