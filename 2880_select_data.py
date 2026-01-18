'''
You are given a DataFrame students with the columns student_id, name, and age.
Write a solution to select and display the name and age of the student whose student_id is 101.
The output should contain only the columns name and age, formatted as shown in the example.

Дан DataFrame students, который содержит столбцы student_id, name и age.
Напишите решение, которое выбирает и выводит имя и возраст студента, у которого student_id равен 101.
В результате должны отображаться только столбцы name и age, как в примере.
'''

import pandas as pd

def select_data(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101, ["name", "age"]]