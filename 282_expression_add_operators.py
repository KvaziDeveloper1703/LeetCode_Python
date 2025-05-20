'''
You are given a string number consisting only of digits, and an integer target.
Return all possible expressions by inserting the binary operators '+', '-', and/or '*' between the digits in number such that the resulting expression evaluates exactly to target.

Constraints:
    + No operand in the expression should have leading zeros;
    + The multiplication operator '*' should follow standard operator precedence rules.

Examples:
Input: number = "123", target = 6
Output: ["1+2+3", "1*2*3"]

Input: number = "232", target = 8
Output: ["2*3+2", "2+3*2"]

Дана строка number, состоящая только из цифр, и целое число target.
Нужно вернуть все возможные варианты вставки бинарных операторов '+', '-' и '*' между цифрами строки number так, чтобы итоговое арифметическое выражение давало в результате значение, равное target.

Условия:
    + Операнды в выражении не должны содержать ведущих нулей;
    + Умножение '*' должно подчиняться стандартным правилам приоритета операторов.

Примеры:
Ввод: number = "123", target = 6
Вывод: ["1+2+3", "1*2*3"]

Ввод: number = "232", target = 8
Вывод: ["2*3+2", "2+3*2"]
'''

from typing import List

class Solution:
    def addOperators(self, number: str, target: int) -> List[str]:
        result = []

        def backtrack(position: int, expression: str, current_value: int, last_operand: int):
            if position == len(number):
                if current_value == target:
                    result.append(expression)
                return
            
            for i in range(position + 1, len(number) + 1):
                current_str = number[position:i]
                if len(current_str) > 1 and current_str[0] == '0':
                    break
                current_int = int(current_str)
                
                if position == 0:
                    backtrack(i, current_str, current_int, current_int)
                else:
                    backtrack(i, expression + '+' + current_str, current_value + current_int, current_int)
                    backtrack(i, expression + '-' + current_str, current_value - current_int, -current_int)
                    backtrack(i, expression + '*' + current_str, current_value - last_operand + last_operand * current_int, last_operand * current_int)

        backtrack(0, "", 0, 0)
        return result