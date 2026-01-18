'''
You are given a DataFrame named employees with the following columns: employee_id, name, department, and salary.

Write a solution that displays the first 3 rows of this DataFrame.

Example:
Input: employees DataFrame
Output: the first 3 rows of employees

Дан DataFrame employees, который содержит столбцы: employee_id, name, department, salary.

Напишите решение, которое выводит первые 3 строки этого DataFrame.

Пример:
Ввод: DataFrame employees
Вывод: первые 3 строки DataFrame employees
'''

import pandas as pd

def select_first_rows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)