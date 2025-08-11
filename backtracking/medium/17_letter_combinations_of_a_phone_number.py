'''
Given a string containing digits from 2-9 inclusive.

Return all possible letter combinations that the number could represent.

A mapping of digits to letters:
2 -> "abc"
3 -> "def"
4 -> "ghi"
5 -> "jkl"
6 -> "mno"
7 -> "pqrs"
8 -> "tuv"
9 -> "wxyz"

Examples:
Input: digits = "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Input: digits = ""
Output: []

Дана строка, содержащая цифры от 2 до 9 включительно. 

Необходимо вернуть все возможные комбинации букв, которые могут быть представлены этими цифрами. 

Сопоставление цифр с буквами следующее:
2 -> "abc"
3 -> "def"
4 -> "ghi"
5 -> "jkl"
6 -> "mno"
7 -> "pqrs"
8 -> "tuv"
9 -> "wxyz"

Примеры:
Ввод: digits = "23"
Вывод: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Ввод: digits = ""
Вывод: []
'''

def letter_сombinations(digits: str):
    if not digits:
        return []

    digit_to_letters = {'2': 'abc', 
                        '3': 'def', 
                        '4': 'ghi', 
                        '5': 'jkl',
                        '6': 'mno', 
                        '7': 'pqrs', 
                        '8': 'tuv', 
                        '9': 'wxyz'
                }

    result = []

    def backtrack(index, path):
        if index == len(digits):
            result.append("".join(path))
            return

        for letter in digit_to_letters[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    backtrack(0, [])
    return result