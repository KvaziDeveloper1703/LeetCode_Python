'''
Given a string S containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    + Open brackets must be closed by the same type of brackets;
    + Open brackets must be closed in the correct order;
    + Every close bracket has a corresponding open bracket of the same type.

Examples:
Input: S = "()"
Output: true

Input: S = "()[]{}"
Output: true

Дана строка S, содержащая только символы '(', ')', '{', '}', '[' и ']'. Определите, является ли эта строка правильной.
Строка считается правильной, если выполняются следующие условия:
    + Открывающие скобки должны закрываться скобками того же типа;
    + Открывающие скобки должны закрываться в правильном порядке;
    + Каждой закрывающей скобке должна соответствовать открывающая скобка того же типа.

Примеры:
Вход: S = "()"
Выход: true

Вход: S = "()[]{}"
Выход: true
'''

def is_valid(S: str) -> bool:
    stack = []
    bracket_map = { ')':'(', 
                    '}':'{', 
                    ']':'['}
    for character in S:
        if character in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[character] != top_element:
                return False
        else:
            stack.append(character)
    return not stack