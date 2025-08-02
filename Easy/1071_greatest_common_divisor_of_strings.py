'''
We say that a string t divides a string s if and only if s can be written as one or more repetitions of t.

Given two strings string_1 and string_2.

Return the largest string x such that x divides both string_1 and string_2.

Examples:
Input: string_1 = "ABCABC", string_2 = "ABC"  
Output: "ABC"

Input: string_1 = "ABABAB", string_2 = "ABAB"  
Output: "AB"

Мы говорим, что строка t делит строку s тогда и только тогда, когда s можно записать как одну или более повторений строки t.

Даны две строки string_1 и string_2.

Нужно вернуть наибольшую строку x, такую что x делит и string_1, и string_2.

Примеры:
Ввод: string_1 = "ABCABC", string_2 = "ABC"  
Вывод: "ABC"

Ввод: string_1 = "ABABAB", string_2 = "ABAB"  
Вывод: "AB"
'''

from math import gcd

def gcd_of_strings(string_1: str, string_2: str) -> str:
    if string_1 + string_2 != string_2 + string_1:
        return ""

    length = gcd(len(string_1), len(string_2))
    return string_1[:length]