'''
You are given a string s and an array of strings words. Determine whether s is a prefix string of words.

A string s is a prefix string of words if it can be formed by concatenating the first k strings in words, for some positive integer k ≤ words.length.

Return True if s is a prefix string of words, and False otherwise.

Examples:
Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: True

Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
Output: False

Дана строка s и массив строк words. Нужно определить, является ли s префиксной строкой массива words.

Строка s считается префиксной, если её можно получить, конкатенируя первые k строк из words, где k - положительное число и k ≤ длине words.

Верните True, если s является префиксной строкой массива words, иначе верните False.

Примеры:
Ввод: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Вывод: True

Ввод: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
Вывод: False
'''

from typing import List

def is_prefix_string(s: str, words: List[str]) -> bool:
    concatenated_string = ""

    for word in words:
        concatenated_string += word
        if concatenated_string == s:
            return True
        if len(concatenated_string) > len(s):
            return False

    return False