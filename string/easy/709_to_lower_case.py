'''
Given a string S, return the string after replacing every uppercase letter with the same lowercase letter.

Examples:
Input: S = "Hello"
Output: "hello"

Input: S = "here"
Output: "here"

Дана строка S. Верните строку, в которой каждая заглавная буква заменена на такую же строчную букву.

Примеры:
Ввод: S = "Hello"
Вывод: "hello"

Ввод: S = "here"
Вывод: "here"
'''

def to_lower_case(S: str) -> str:
    return S.lower()