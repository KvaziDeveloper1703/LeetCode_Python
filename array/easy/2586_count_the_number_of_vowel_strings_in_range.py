'''
You are given a 0-indexed array of strings words and two integers left and right.

A string is called a vowel string if it starts with a vowel and ends with a vowel. Vowel characters are: 'a', 'e', 'i', 'o', and 'u'.

Return the number of vowel strings words[i] such that the index i belongs to the inclusive range [left, right].

Examples:
Input: words = ["are", "amy", "u"], left = 0, right = 2
Output: 2

Input: words = ["hey", "aeo", "mu", "ooo", "artro"], left = 1, right = 4
Output: 3

Дан массив строк words с нумерацией с нуля и два целых числа left и right.

Строка называется гласной строкой, если она начинается с гласной буквы и заканчивается гласной буквой. Гласные буквы: 'a', 'e', 'i', 'o' и 'u'.

Верните количество гласных строк words[i], для которых индекс i принадлежит включительному диапазону [left, right].

Примеры:
Ввод: words = ["are", "amy", "u"], left = 0, right = 2
Вывод: 2

Ввод: words = ["hey", "aeo", "mu", "ooo", "artro"], left = 1, right = 4
Вывод: 3
'''

from typing import List

def vowel_strings(words: List[str], left: int, right: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0

    for i in range(left, right + 1):
        if words[i][0] in vowels and words[i][-1] in vowels:
            count += 1

    return count