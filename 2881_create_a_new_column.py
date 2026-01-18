'''
You are given a DataFrame employees with two columns: name and salary.
A company wants to give employees a bonus.
Write a solution to create a new column called bonus, where each value is twice the value of the salary column.
The output DataFrame should include the columns name, salary, and bonus, as shown in the example.

Дан DataFrame employees, содержащий два столбца: name и salary.
Компания планирует выдать сотрудникам бонус.
Напишите решение, которое создаёт новый столбец bonus, в котором каждое значение равно удвоенной зарплате из столбца salary.
В результате должны быть показаны столбцы name, salary и bonus, как в примере.
'''

import pandas as pd

def create_bonus_column(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees