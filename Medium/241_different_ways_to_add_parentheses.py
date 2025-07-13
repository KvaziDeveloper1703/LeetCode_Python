'''
Given a string expression of numbers and operators (+, -, *).

Return all possible results from computing all the different possible ways to group numbers and operators. You may return the answers in any order.

It is guaranteed that:
    + The results will fit in a 32-bit integer;
    + The number of different results will not exceed 10⁴.

Examples:
Input: expression = "2-1-1"
Output: [0,2]

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]

Дана строка expression, содержащая числа и знаки операторов (+, - и *).

Необходимо вернуть все возможные результаты вычислений, которые получаются при различных способах расстановки скобок. Можно вернуть результаты в любом порядке.

Гарантируется, что:
    + Все результаты помещаются в 32-битное целое число;
    + Количество различных результатов не превышает 10⁴.

Примеры:
Ввод: expression = "2-1-1"
Вывод: [0, 2]

Ввод: expression = "2*3-4*5"
Вывод: [-34, -14, -10, -10, 10]
'''

from typing import List

def diff_ways_to_compute(expression: str) -> List[int]:
    computed_cache = {}

    def compute_all_ways(sub_expression: str) -> List[int]:
        if sub_expression in computed_cache:
            return computed_cache[sub_expression]

        possible_results = []
        for index, operator in enumerate(sub_expression):
            if operator in "+-*":
                left_combinations = compute_all_ways(sub_expression[:index])
                right_combinations = compute_all_ways(sub_expression[index+1:])
                for left_value in left_combinations:
                    for right_value in right_combinations:
                        if operator == '+':
                            possible_results.append(left_value + right_value)
                        elif operator == '-':
                            possible_results.append(left_value - right_value)
                        else:
                            possible_results.append(left_value * right_value)

        if not possible_results:
            possible_results.append(int(sub_expression))

        computed_cache[sub_expression] = possible_results
        return possible_results

    return compute_all_ways(expression)