'''
You are given an array of strings words and a string s.

The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words, taken in the same order.

Return True if s is an acronym of words, and False otherwise.

Examples:
Input: words = ["alice", "bob", "charlie"], s = "abc"
Output: True

Input: words = ["an", "apple"], s = "a"
Output: False

Дан массив строк words и строка s.

Строка s считается акронимом массива words, если она может быть получена путём конкатенации первых символов каждой строки из words, взятых в том же порядке.

Верните True, если s является акронимом массива words, и False в противном случае.

Примеры:
Ввод: words = ["alice", "bob", "charlie"], s = "abc"
Вывод: True

Ввод: words = ["an", "apple"], s = "a"
Вывод: False
'''

from typing import List

def is_acronym(words: List[str], s: str) -> bool:
    if len(words) != len(s):
        return False

    for i in range(len(words)):
        if words[i][0] != s[i]:
            return False

    return True