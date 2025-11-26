'''
There is a programming language with only four operations and one variable X:
    - ++X and X++ increase the value of X by 1;
    - --X and X-- decrease the value of X by 1.

Initially, X = 0.

Given an array of strings operations representing a list of operations, return the final value of X after performing all of them.

Examples:
Input: operations = ["--X","X++","X++"]
Output: 1

Input: operations = ["++X","++X","X++"]
Output: 3

Есть язык программирования, в котором существует только четыре операции и одна переменная X:
    - ++X и X++ увеличивают значение X на 1;
    - --X и X-- уменьшают значение X на 1.

Изначально X = 0.

Дан массив строк operations, который содержит список операций. Нужно вернуть итоговое значение X после выполнения всех операций.

Примеры:
Ввод: operations = ["--X","X++","X++"]
Вывод: 1

Ввод: operations = ["++X","++X","X++"]
Вывод: 3
'''

from typing import List

def final_value_after_operations(operations: List[str]) -> int:
    variable_value = 0

    for operation in operations:
        if "++" in operation:
            variable_value += 1
        else:
            variable_value -= 1

    return variable_value