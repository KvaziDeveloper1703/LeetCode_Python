'''
Given two strings, S and T, return true if T is an anagram of S, and false otherwise.
An anagram is a word formed from the same letters as another word, with the same number of each letter, but in a different order.

Examples:
Input: S = "anagram", T = "nagaram"
Output: true

Input: S = "rat", T = "car"
Output: false

Даны две строки S и T. Необходимо вернуть true, если T является анаграммой строки S, и false — в противном случае.
Анаграмма — это слово, составленное из тех же букв, что и другое слово, с тем же количеством каждой буквы, но в другом порядке.

Примеры:
Ввод: S = "anagram", T = "nagaram"
Вывод: true

Ввод: S = "rat", T = "car"
Вывод: false
'''

def is_anagram(S: str, T: str) -> bool:
    if len(S) != len(T):
        return False
    return sorted(S) == sorted(T)