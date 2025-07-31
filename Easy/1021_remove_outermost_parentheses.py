'''
Given a valid parentheses string S.
A valid parentheses string is primitive if it is non-empty and cannot be split into two non-empty valid parentheses strings.

Return the string after removing the outermost parentheses of every primitive part of s.

Examples:
Input: S = "(()())(())"
Output: "()()()"

Input: S = "(()())(())(()(()))"
Output: "()()()()(())"

Дана корректная строка скобок S.
Строка считается примитивной, если она непустая и не может быть разделена на две непустые корректные строки.

Верните строку, удалив внешние скобки у каждой примитивной части s.

Примеры:
Ввод: S = "(()())(())"
Вывод: "()()()"

Ввод: S = "(()())(())(()(()))"
Вывод: "()()()()(())"
'''

def remove_outer_parentheses(S: str) -> str:
    result = []
    balance = 0

    for character in S:
        if character == '(':
            if balance > 0:
                result.append(character)
            balance += 1
        else:
            balance -= 1
            if balance > 0:
                result.append(character)

    return ''.join(result)