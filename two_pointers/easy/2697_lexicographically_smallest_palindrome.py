'''
You are given a string s consisting of lowercase English letters. You are allowed to perform operations on this string.

In one operation, you can replace any single character in s with any other lowercase English letter.

Your task is to transform s into a palindrome using the minimum number of operations.

If there are multiple palindromes that can be obtained with the minimum number of operations, you should return the lexicographically smallest one.

A string a is considered lexicographically smaller than a string b (of the same length) if, at the first position where they differ, string a has a character that appears earlier in the alphabet than the corresponding character in b.

Return the resulting palindrome string.

Examples:
Input: s = "egcfe"
Output: "efcfe"

Input: s = "abcd"
Output: "abba"

Дана строка s, состоящая из строчных латинских букв. Разрешается выполнять операции над этой строкой.

За одну операцию можно заменить любой один символ в строке s на любой другой строчный латинский символ.

Необходимо превратить строку s в палиндром, используя минимальное возможное количество операций.

Если существует несколько палиндромов, которые можно получить с минимальным числом операций, требуется вернуть лексикографически наименьший из них.

Строка a считается лексикографически меньшей, чем строка b (одинаковой длины), если в первой позиции, где они различаются, символ в строке a стоит раньше в алфавите, чем соответствующий символ в строке b.

Верните получившуюся палиндромную строку.

Примеры:
Ввод: s = "egcfe"
Вывод: "efcfe"

Ввод: s = "abcd"
Вывод: "abba"
'''

def make_smallest_palindrome(s: str) -> str:
    characters = list(s)
    left = 0
    right = len(characters) - 1

    while left < right:
        if characters[left] != characters[right]:
            smaller_character = min(characters[left], characters[right])
            characters[left] = smaller_character
            characters[right] = smaller_character

        left += 1
        right -= 1

    return "".join(characters)