'''
Given a string S, reverse only all the vowels in the string and return the resulting string.

Examples:
Input: S = "IceCreAm"
Output: "AceCreIm"

Input: S = "leetcode"
Output: "leotcede"

Дана строка S. Необходимо перевернуть только все гласные в этой строке и вернуть получившуюся строку.

Примеры:
Ввод: S = "IceCreAm"
Вывод: "AceCreIm"

Ввод: S = "leetcode"
Вывод: "leotcede"
'''

def reverse_vowels(S: str) -> str:
    vowels = set('aeiouyAEIOUY')
    S_list = list(S)
    left, right = 0, len(S_list) - 1

    while left < right:
        while left < right and S_list[left] not in vowels:
            left += 1
        while left < right and S_list[right] not in vowels:
            right -= 1

        S_list[left], S_list[right] = S_list[right], S_list[left]
        left += 1
        right -= 1

    return ''.join(S_list)