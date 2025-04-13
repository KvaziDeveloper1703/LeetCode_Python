'''
Given a string S representing a valid mathematical expression, implement a basic calculator to evaluate it and return the result. 
You are not allowed to use built-in functions like eval().

Examples:
Input: "1 + 1"
Output: 2

Input: "2 - 1 + 2"
Output: 3

Дана строка S, представляющая корректное математическое выражение.
Необходимо реализовать простой калькулятор, который вычисляет значение этого выражения и возвращает результат.
Нельзя использовать встроенные функции, такие как eval().

Примеры:
Ввод: "1 + 1"
Вывод: 2

Ввод: "2 - 1 + 2"
Вывод: 3
'''

def calculate(expression: str) -> int:
    stack = []
    current_number = 0
    result = 0
    sign = 1

    for character in expression:
        if character.isdigit():
            current_number = current_number * 10 + int(character)

        elif character == "+":
            result += sign * current_number
            current_number = 0
            sign = 1

        elif character == "-":
            result += sign * current_number
            current_number = 0
            sign = -1

        elif character == "(":
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1

        elif character == ")":
            result += sign * current_number
            current_number = 0

            result *= stack.pop()
            result += stack.pop()

        elif character == " ":
            continue

    result += sign * current_number
    return result