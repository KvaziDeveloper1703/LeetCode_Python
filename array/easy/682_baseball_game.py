'''
You are keeping score for a baseball game with unusual rules.
At the start of the game, your record is empty.

Given a list of strings operations, where each operations[i] is the i-th operation you must perform on the record.
Each operation is one of the following:
    + An integer x: Record a new score of value x;
    + '+': Record a new score equal to the sum of the previous two scores;
    + 'D': Record a new score equal to double the previous score;
    + 'C': Remove the previous score from the record.

After applying all operations, return the sum of all the scores in the record.

Examples:
Input: operations = ["5","2","C","D","+"]
Output: 30

Input: operations = ["5","-2","4","C","D","9","+","+"]
Output: 27

Вы ведёте счёт бейсбольной игры с необычными правилами.
Изначально ваш список очков пуст.

Дан список строк operations, где каждая operations[i] — это i-я операция, которую нужно выполнить над списком. 
Каждая операция может быть одной из следующих:
    + Целое число x: Добавьте в список новый результат со значением x;
    + '+': Добавьте новый результат, который равен сумме двух предыдущих результатов;
    + 'D': Добавьте новый результат, который равен удвоенному предыдущему результату;
    + 'C': Удалите предыдущий результат из списка.

После выполнения всех операций верните сумму всех значений в списке.

Примеры:
Ввод: operations = ["5","2","C","D","+"]
Вывод: 30

Ввод: operations = ["5","-2","4","C","D","9","+","+"]
Вывод: 27
'''

from typing import List

def calculate_points(operations: List[str]) -> int:
    stack = []

    for operation in operations:
        if operation == "C":
            stack.pop()
        elif operation == "D":
            stack.append(2 * stack[-1])
        elif operation == "+":
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(operation))

    return sum(stack)