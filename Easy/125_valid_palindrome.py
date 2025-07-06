'''
A palindrome is a phrase that reads the same forward and backward after:
    + Converting all letters to lowercase;
    + Removing all non-alphanumeric characters.

Given a string S, return True if it is a palindrome, otherwise return False.

Examples:
Input: S = "A man, a plan, a canal: Panama"
Output: True

Input: S = "race a car"
Output: False

Палиндром — это фраза, которая читается одинаково слева направо и справа налево после следующих преобразований:
    + Все буквы приводятся к нижнему регистру;
    + Удаляются все неалфавитно-цифровые символы.

Дана строка S. Верните True, если она является палиндромом, и False — в противном случае.

Примеры:
Ввод: S = "A man, a plan, a canal: Panama"
Вывод: True

Ввод: S = "race a car"
Вывод: False
'''

def is_palindrome(S: str) -> bool:
    lower_case_string = S.lower()

    cleaned = ''
    for character in lower_case_string:
        if character.isalnum():
            cleaned += character

    reversed_cleaned = ''
    for i in range(len(cleaned) - 1, -1, -1):
        reversed_cleaned += cleaned[i]

    if cleaned == reversed_cleaned:
        return True
    else:
        return False