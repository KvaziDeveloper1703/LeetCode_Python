'''
Given a valid parentheses string S.

The nesting depth of S is defined as the maximum number of parentheses that are nested inside each other.

Return the nesting depth of the string.

Examples:
Input: S = "(1+(2*3)+((8)/4))+1"
Output: 3

Input: S = "(1)+((2))+(((3)))"
Output: 3

Дана правильная скобочная строка S.

Глубина вложенности строки определяется как максимальное количество скобок, находящихся одна внутри другой.

Нужно вернуть глубину вложенности строки.

Примеры:
Ввод: S = "(1+(2*3)+((8)/4))+1"
Вывод: 3

Ввод: S = "(1)+((2))+(((3)))"
Вывод: 3
'''

def max_depth(S: str) -> int:
    current_depth = 0
    max_depth = 0

    for character in S:
        if character == '(':
            current_depth += 1
            if current_depth > max_depth:
                max_depth = current_depth
        elif character == ')':
            current_depth -= 1

    return max_depth