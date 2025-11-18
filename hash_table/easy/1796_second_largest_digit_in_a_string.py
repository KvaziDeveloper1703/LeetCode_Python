'''
You are given an alphanumeric string s.
Your task is to return the second largest numerical digit that appears in s.
If s does not contain at least two different digits, return -1.

An alphanumeric string consists of lowercase English letters and digits.

Examples:
Input: s = "dfa12321afd"
Output: 2

Input: s = "abc1111"
Output: -1

Дана алфавитно-цифровая строка s.
Требуется вернуть вторую по величине цифру, которая встречается в этой строке.
Если в строке нет хотя бы двух разных цифр, вернуть -1.

Алфавитно-цифровая строка - это строка, состоящая из строчных латинских букв и цифр.

Примеры:
Ввод: s = "dfa12321afd"
Вывод: 2

Ввод: s = "abc1111"
Вывод: -1
'''

def second_highest(input_string: str) -> int:
    unique_digits: set[int] = {int(character) for character in input_string if character.isdigit()}
    if len(unique_digits) < 2:
        return -1
    sorted_unique_digits_descending: list[int] = sorted(unique_digits, reverse=True)
    return sorted_unique_digits_descending[1]