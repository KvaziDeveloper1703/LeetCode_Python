'''
You are given two strings, sequence and word.

A string word is said to be k-repeating in sequence if the string formed by concatenating word exactly k times is a substring of sequence.

The maximum k-repeating value of word in sequence is the largest integer k for which word repeated k times is still a substring of sequence.

If word does not appear as a substring of sequence at all, then its maximum k-repeating value is 0.

Return the maximum k-repeating value of word in sequence.

Examples:
Input: sequence = "ababc", word = "ab"
Output: 2

Input: sequence = "ababc", word = "ba"
Output: 1

Даны две строки: sequence и word.

Строка word называется k-повторяющейся в строке sequence, если строка, образованная повторением word подряд k раз, является подстрокой sequence.

Максимальное значение k-повторения - это наибольшее число k, для которого word, повторённое k раз, всё ещё содержится как подстрока в sequence.

Если word вообще не встречается в sequence, то значение k равно 0.

Нужно вернуть это максимальное значение k.

Примеры:
Ввод: sequence = "ababc", word = "ab"
Вывод: 2

Ввод: sequence = "ababc", word = "ba"
Вывод: 1
'''

def max_repeating(sequence: str, word: str) -> int:
    k = 0
    pattern = word
    while pattern in sequence:
        k += 1
        pattern += word
    return k