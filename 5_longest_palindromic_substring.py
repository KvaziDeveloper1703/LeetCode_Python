'''
Given a string S, return the longest palindromic substring in S.

Example:
Input: S = "babad"
Output: "bab"

Дана строка S. Необходимо вернуть самую длинную подстроку-палиндром в этой строке.

Пример:
Ввод: S = "babad"
Вывод: "bab"
'''

def longest_palindrome(S: str) -> str:
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(S) and S[left] == S[right]:
            left -= 1
            right += 1
        return S[left + 1:right]
    longest = ""
    for i in range(len(S)):
        palindrome_1 = expand_around_center(i, i)
        palindrome_2 = expand_around_center(i, i + 1)
        if len(palindrome_1) > len(longest):
            longest = palindrome_1
        if len(palindrome_2) > len(longest):
            longest = palindrome_2
    return longest