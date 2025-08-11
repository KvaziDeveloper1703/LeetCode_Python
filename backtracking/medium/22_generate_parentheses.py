'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example:
Input: n = 3
Output: [   "((()))", 
            "(()())", 
            "(())()", 
            "()(())", 
            "()()()"
    ]

Дано n пар скобок. Напишите функцию, которая генерирует все возможные комбинации правильно сбалансированных скобок.

Пример:
Ввод: n = 3
Вывод: ["((()))", 
        "(()())", 
        "(())()", 
        "()(())", 
        "()()()"
    ]
'''

def generate_parenthesis(n: int) -> list[str]:
    result = []

    def backtrack(current_string, open_count, close_count):
        if len(current_string) == 2 * n:
            result.append(current_string)
            return

        if open_count < n:
            backtrack(current_string + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current_string + ')', open_count, close_count + 1)

    backtrack("", 0, 0)
    return result