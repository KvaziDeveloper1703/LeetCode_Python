'''
Write a function that reverses a string.

The input string is provided as an array of characters S.
You must reverse the string in-place, using O(1) extra memory.

Examples:
Input: S = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: S = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Напиши функцию, которая переворачивает строку.

Входная строка задаётся в виде массива символов S.
Ты должен перевернуть строку на месте, используя O(1) дополнительной памяти.

Примеры:
Ввод: S = ["h","e","l","l","o"]
Вывод: ["o","l","l","e","h"]

Ввод: S = ["H","a","n","n","a","h"]
Вывод: ["h","a","n","n","a","H"]
'''

def reverse_string(S: List[str]) -> None:
    left, right = 0, len(S) - 1
    while left < right:
        S[left], S[right] = S[right], S[left]
        left += 1
        right -= 1