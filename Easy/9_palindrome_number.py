'''
Given an integer n, return true if n is a palindrome, and false otherwise.

Examples:
Input: n = 121
Output: true

Input: n = -121
Output: false

Дано целое число n. Верните true, если n является палиндромом, и false — в противном случае.

Примеры:
Ввод: n = 121
Вывод: true

Ввод: n = -121
Вывод: false
'''

def is_palindrome(n: int) -> bool:
    if n < 0:
        return False
    if n != 0 and n % 10 == 0:
        return False
    reversed_half = 0
    while n > reversed_half:
        reversed_half = reversed_half * 10 + n % 10
        n //= 10
    return n == reversed_half or n == reversed_half // 10