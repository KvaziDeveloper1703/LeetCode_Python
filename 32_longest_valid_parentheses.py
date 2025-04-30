'''
You are given a string S consisting only of the characters '(' and ')'. Your task is to return the length of the longest valid (well-formed) parentheses substring.
A valid substring is one where every opening parenthesis has a corresponding closing one, and all parentheses are properly nested.

Examples:
Input: S = "(()"
Output: 2

Input: S = ")()())"
Output: 4

Дана строка S, состоящая только из символов '(' и ')'. Необходимо вернуть длину самой длинной корректной (правильно вложенной) подстроки с круглыми скобками.
Корректной считается подстрока, в которой каждая открывающая скобка имеет соответствующую закрывающую, и все скобки правильно вложены.

Примеры:
Ввод: S = "(()"
Вывод: 2

Ввод: S = ")()())"
Вывод: 4
'''

def longest_valid_parentheses(S: str) -> int:
    max_len = 0
    stack = [-1]
    for i, character in enumerate(S):
        if character == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len