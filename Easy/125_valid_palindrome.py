'''
A palindrome is a phrase that reads the same forward and backward after:
+ Converting all letters to lowercase;
+ Removing all non-alphanumeric characters.

Given a string S, return true if it is a palindrome, otherwise return false.

Examples:
Input: S = "A man, a plan, a canal: Panama"
Output: true

Input: S = "race a car"
Output: false

Палиндром — это фраза, которая читается одинаково слева направо и справа налево после следующих преобразований:
Все буквы приводятся к нижнему регистру;
Удаляются все неалфавитно-цифровые символы (пробелы, знаки препинания и т. д.).

Дана строка S. Верните true, если она является палиндромом, и false — в противном случае.

Примеры:
Вход: S = "A man, a plan, a canal: Panama"
Выход: true

Вход: S = "race a car"
Выход: false
'''

def is_palindrome(S: str) -> bool:
    cleaned = ''.join(character.lower() for character in S if character.isalnum())
    return cleaned == cleaned[::-1]