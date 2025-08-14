'''
Given an alphanumeric string S.

You need to rearrange the characters of S so that:
    + No letter is immediately followed by another letter;
    + No digit is immediately followed by another digit.

In other words, no two adjacent characters can be of the same type.

Return the reformatted string, or return an empty string "" if it is impossible to rearrange the string to satisfy the condition.

Examples:
Input: S = "a0b1c2"
Output: "0a1b2c"

Input: S = "leetcode"
Output: ""

Дана буквенно-цифровая строка S.

Необходимо переставить символы строки так, чтобы:
    + Ни одна буква не стояла сразу после другой буквы;
    + Ни одна цифра не стояла сразу после другой цифры.

Иными словами, два соседних символа не могут быть одного типа.

Нужно вернуть переформатированную строку, либо пустую строку "", если невозможно удовлетворить условие.

Примеры:
Ввод: S = "a0b1c2"
Вывод: "0a1b2c"

Ввод: S = "leetcode"
Вывод: ""
'''

def reformat(S: str) -> str:
    digits = []
    letters = []
    for character in S:
        if character.isdigit():
            digits.append(character)
        elif character.isalpha():
            letters.append(character)

    if len(digits) - len(letters) > 1 or len(letters) - len(digits) > 1:
        return ""

    if len(digits) >= len(letters):
        first = digits
        second = letters
    else:
        first = letters
        second = digits

    result = []
    i = 0
    j = 0
    while i < len(first) or j < len(second):
        if i < len(first):
            result.append(first[i])
            i += 1
        if j < len(second):
            result.append(second[j])
            j += 1

    return "".join(result)