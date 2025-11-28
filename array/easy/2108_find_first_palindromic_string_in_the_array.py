'''
You are given an array of strings words.

Your task is to return the first palindromic string in the array.

If no palindromic string exists, return an empty string "".

A string is palindromic if it reads the same forward and backward.

Examples:
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"

Input: words = ["notapalindrome","racecar"]
Output: "racecar"

Дан массив строк words.

Необходимо вернуть первую палиндромную строку в этом массиве.

Если палиндромов нет, верните пустую строку "".

Строка является палиндромом, если она читается одинаково слева направо и справа налево.

Примеры:
Ввод: words = ["abc","car","ada","racecar","cool"]
Вывод: "ada"

Ввод: words = ["notapalindrome","racecar"]
Вывод: "racecar"
'''

from typing import List

def first_palindrome(words: List[str]) -> str:
    for word in words:
        if word == word[::-1]:
            return word
    return ""