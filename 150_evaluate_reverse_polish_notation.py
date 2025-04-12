'''
You are given an array of strings tokens that represents an arithmetic expression in Reverse Polish Notation.
Evaluate the expression and return an integer that represents the value of the expression.

Notes:
+ The valid operators are +, -, *, and /;
+ Each operand may be an integer or another expression;
+ The division between two integers always truncates toward zero;
+ There will not be any division by zero;
+ The input represents a valid arithmetic expression in Reverse Polish Notation;
+ The answer and all the intermediate calculations can be represented in a 32-bit integer.

Examples:
Input: tokens = ["2","1","+","3","*"]
Output: 9

Input: tokens = ["4","13","5","/","+"] 
Output: 6

Дан массив строк tokens, представляющий арифметическое выражение в обратной польской записи.
Необходимо вычислить значение выражения и вернуть целое число, которое является результатом вычислений.

Условия:
+ Допустимые операторы: +, -, *, /;
+ Каждый операнд может быть целым числом или другим выражением;
+ Деление двух целых чисел всегда округляется к нулю;
+ Деления на ноль не будет;
+ Входные данные всегда представляют корректное арифметическое выражение в RPN;
+ Результат и все промежуточные вычисления можно выразить в пределах 32-битного целого числа.

Примеры:
Ввод: tokens = ["2", "1", "+", "3", "*"]
Вывод: 9

Ввод: tokens = ["4", "13", "5", "/", "+"]
Вывод: 6
'''

from typing import List

def evaluate_rpn(tokens: List[str]) -> int:
    stack = []

    for token in tokens:
        if token in "+-*/":
            second_operand = stack.pop()
            first_operand = stack.pop()

            if token == "+":
                stack.append(first_operand + second_operand)
            elif token == "-":
                stack.append(first_operand - second_operand)
            elif token == "*":
                stack.append(first_operand * second_operand)
            elif token == "/":
                stack.append(int(first_operand / second_operand))
        else:
            stack.append(int(token))

    return stack[0]