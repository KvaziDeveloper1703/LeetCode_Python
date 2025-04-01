'''
You are given an array of strings tokens that represents an arithmetic expression in Reverse Polish Notation (RPN).
Evaluate the expression and return an integer that represents the value of the expression.

Notes:
+ The valid operators are +, -, *, and /.
+ Each operand may be an integer or another expression.
+ The division between two integers always truncates toward zero.
+ There will not be any division by zero.
+ The input represents a valid arithmetic expression in Reverse Polish Notation.
+ The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9

Example 2:
Input: tokens = ["4","13","5","/","+"] 
Output: 6
'''

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]