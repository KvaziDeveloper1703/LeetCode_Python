'''
You are given a 0-indexed string word consisting only of lowercase English letters.

You must choose exactly one index and remove the character at that index from word so that the frequency of every remaining letter is the same.

Return True if it is possible to remove exactly one character such that all letters in the resulting string have equal frequency. Otherwise, return False.

Notes:
    - The frequency of a letter is the number of times it appears in the string;
    - You must remove exactly one character; choosing to remove none is not allowed.

Examples:
Input: word = "abcc"
Output: True

Input: word = "aazz"
Output: False

Вам дана строка word с нулевой индексацией, состоящая только из строчных английских букв.

Необходимо выбрать ровно один индекс и удалить символ по этому индексу так, чтобы частота всех оставшихся букв стала одинаковой.

Верните True, если существует возможность удалить ровно один символ, после чего частота всех букв в строке будет одинаковой. В противном случае верните False.

Примечания
    - Частота буквы - это количество её вхождений в строку;
    - Удалить ровно один символ обязательно; вариант без удаления не допускается.

Примеры:
Ввод: word = "abcc"
Вывод: True

Ввод: word = "aazz"
Вывод: False
'''

from collections import Counter

def equal_frequency(word: str) -> bool:
    frequency = Counter(word)

    for character in list(frequency.keys()):
        frequency[character] -= 1

        if frequency[character] == 0:
            del frequency[character]

        if len(set(frequency.values())) == 1:
            return True

        frequency = Counter(word)

    return False