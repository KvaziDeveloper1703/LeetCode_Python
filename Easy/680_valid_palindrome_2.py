'''
Given a string S. Your task is to determine whether it is possible to make S a palindrome by deleting at most one character.

Return True if you can make S a palindrome after at most one deletion; otherwise, return False.

Examples:
Input: S = "aba"
Output: True

Input: S = "abca"
Output: True

Дана строка S. Нужно определить, можно ли сделать эту строку палиндромом, удалив не более одного символа.

Если это возможно, верните True; в противном случае — False.

Примеры:
Ввод: S = "aba"
Вывод: True

Ввод: S = "abca"
Вывод: True
'''

def valid_palindrome(S: str) -> bool:

    def is_palindrome_range(left: int, right: int) -> bool:
        while left < right:
            if S[left] != S[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(S) - 1
        
    while left < right:
        if S[left] != S[right]:
            return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
        left += 1
        right -= 1

    return True