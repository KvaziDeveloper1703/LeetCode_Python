'''
You are given a string s. Return True if s is a good string, and False otherwise.

A string is considered good if all characters that appear in it occur the same number of times.

Examples:
Input: s = "abacbc"
Output: True

Input: s = "aaabb"
Output: False

Дана строка s. Верните True, если s является хорошей строкой, и False - в противном случае.

Строка считается хорошей, если все символы, которые в ней встречаются, встречаются одинаковое количество раз.

Примеры:
Ввод: s = "abacbc"
Вывод: True

Ввод: s = "aaabb"
Вывод: False
'''

def are_occurrences_equal(s: str) -> bool:
    character_frequency = {}

    for character in s:
        character_frequency[character] = character_frequency.get(character, 0) + 1

    frequencies_list = list(character_frequency.values())

    return len(set(frequencies_list)) == 1