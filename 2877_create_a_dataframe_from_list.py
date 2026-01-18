'''
Write a solution that creates a Pandas DataFrame from a 2D list named student_data.
Each inner list contains two values: a student's ID and their age.

The DataFrame must have two columns: student_id and age, and it must keep the same row order as in the original student_data list.

Example:
Input: student_data = [ [1, 15],
                        [2, 11],
                        [3, 11],
                        [4, 20]
                ]

Output:
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+

Напишите решение, которое создаёт DataFrame Pandas из двумерного списка student_data.
Каждый вложенный список содержит два значения: ID студента и его возраст.

DataFrame должен иметь два столбца: student_id и age, и сохранять порядок строк таким же, как в исходном списке student_data.

Пример:

Ввод:
student_data = [[1, 15],
                [2, 11],
                [3, 11],
                [4, 20]
        ]

Вывод:
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+
'''

import pandas as pd
from typing import List

def create_dataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=["student_id", "age"])