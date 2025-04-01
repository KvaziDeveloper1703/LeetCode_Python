'''
Given a string s representing a valid mathematical expression, implement a basic calculator to evaluate it and return the result. You are not allowed to use built-in functions like eval().

Examples:
Input: "1 + 1"
Output: 2

Input: " 2-1 + 2 "
Output: 3

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
'''

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        result = 0
        sign = 1
        
        for i in range(len(s)):
            char = s[i]
            
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            
            elif char == "+":
                result += sign * current_number
                current_number = 0
                sign = 1
                
            elif char == "-":
                result += sign * current_number
                current_number = 0
                sign = -1
                
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
                
            elif char == ")":
                result += sign * current_number
                current_number = 0
                
                result *= stack.pop()
                result += stack.pop()
        
        result += sign * current_number
        
        return result